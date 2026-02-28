use std::collections::HashMap;
use std::env::current_dir;
use std::fs;
use std::env;
use std::fs::remove_file;
use std::path::Path;
use chacha20poly1305::aead::rand_core::RngCore;
use std::path::PathBuf;
use chacha20poly1305::{aead::{Aead, KeyInit, OsRng}, ChaCha20Poly1305, Nonce};
use serde_json::Value;
use colored::*;


fn main() {
    let types_path = "C:/Tools/configurations/properties/properties.types";
    let json_data = get_json(types_path);

    let ext_map = build_extension_map(&json_data);

    let args: Vec<String> = env::args().collect();

    if args.len() > 3 {
        let command = &args[1];
        let for_what = &args[2];
        let path = &args[3];

        match command.as_str() {
            "-rmempty" => {
                match for_what.as_str() {
                    "-dir" => {
                        let start_time = std::time::Instant::now();
                        empty_removal(&path, "").expect("Couldn't remove empty folders...");
                        let dur = start_time.elapsed();

                        println!("{} {:.2}s", "Removal took:".bright_cyan(), dur.as_secs_f64());
                        
                    }
                    _ => {
                        println!("{}", "Unknown command".red());
                    }
                }
            }
            "-encrypt" => {
                let path = &args[2];
                let key_str = &args[3];

                let key_bytes = if key_str == "-keygen" {
                    let key = ChaCha20Poly1305::generate_key(&mut OsRng);

                    println!("{} {}", "Generated key:".bright_cyan(), hex::encode(&key));
                    println!("{}", "Save this key! Without it you can't decrypt!".red());
                    key
                } else {
                    let bytes = hex::decode(key_str).expect("Invalid key format!");
                    *chacha20poly1305::Key::from_slice(&bytes)
                };

                let cipher = ChaCha20Poly1305::new(&key_bytes);

                encrypt(Path::new(path), &cipher).expect("Encryption failed!");
            }
            "-decrypt" => {
                let path = &args[2];
                let key_str = &args[3];

                let bytes = hex::decode(key_str).expect("Invalid key format!");

                let key_bytes = *chacha20poly1305::Key::from_slice(&bytes);

                let cipher = ChaCha20Poly1305::new(&key_bytes);

                decrypt(Path::new(path), &cipher).expect("Decryption failed!");
            }
            _ => {
                println!("{}", "Unknown command".red());
            }
        }
    }

    else if args.len() > 2 {
        let command = &args[1];
        let path = &args[2];

        match command.as_str() {
            "-sort" => {
                let start_time = std::time::Instant::now();
                sort(path, &ext_map).expect("Couldn't sort, please try again...");
                let dur = start_time.elapsed();

                println!("{} {:.2}s", "Sorting took:".bright_cyan(), dur.as_secs_f64());
            }
            _ => {
                println!("{}", "Command not found!".red());
            }
        }
    }
    else if args.len() > 1 {
        let command = &args[1];

        match command.as_str() {
            "-keygen" => {
                let key = ChaCha20Poly1305::generate_key(&mut OsRng);
                println!("{} {}", "Generated key:".bright_cyan(), hex::encode(&key));
                println!("{}", "Save this key! Without it you can't decrypt!".red());
            }
            "--version" => {
                println!("{}", env!("CARGO_PKG_VERSION"));
            }
            _ => {
                println!("{}", "Unknown command".red());
            }
        }
    }

    else {
        println!("{}\n{}", "You haven't written any argument.".red(), "Usage: https://github.com/Vova-Professor/SorterW".green());
    }
}


fn build_extension_map(json_data: &Value) -> HashMap<String, String> {
    let mut map = HashMap::new();

    if let Some(categories) = json_data.get("en").and_then(Value::as_object) {
        for (dir_name, ext_list) in categories {
            if let Some(ext_array) = ext_list.as_array() {
                for ext in ext_array {
                    if let Some(e) = ext.as_str() {
                        map.insert(e.to_lowercase(), dir_name.clone());
                    }
                }
            }
        }
    }
    map
}


fn get_json(path: &str) -> Value {
    let content = fs::read_to_string(path).expect("Check if properties.types is in ./configurations/properties/");

    serde_json::from_str(&content).expect("JSON file is corrupted")
}

fn empty_removal(path: &str, relative: &str) -> std::io::Result<()> {
    let base_path = if path == "." {
        current_dir()?
    } else {
        PathBuf::from(path)
    };

    for entry in fs::read_dir(&base_path)? {
        let entry = entry?;
        let dir_path = entry.path();

        if !dir_path.is_dir() {
            continue;
        }
        let folder_name = dir_path.file_name().unwrap().to_str().unwrap();

        let rel = if relative.is_empty() {
            folder_name.to_string()
        } else {
            format!("{}/{}", relative, folder_name)
        };

        println!("{} {}", "Found folder: ".truecolor(169, 169, 169), rel);

        empty_removal(dir_path.to_str().unwrap(), &rel)?;

        let is_empty = fs::read_dir(&dir_path)?.next().is_none();

        if is_empty {
            fs::remove_dir_all(&dir_path)?;
            println!("{} {}", rel, "successfully removed!".bright_magenta());
        }
    }

    Ok(())
}



fn sort(path: &str, ext_map: &HashMap<String, String>) -> std::io::Result<()> {
    let base_path = if path == "." {
        current_dir()?
    } else {
        PathBuf::from(path)
    };

    for entry in fs::read_dir(&base_path)? {
        let entry = entry?;
        let file_path = entry.path();

        if !file_path.is_file() {
            continue;
        }

        let Some(ext) = file_path.extension().and_then(|e| e.to_str()) else {
            continue;
        };

        let ext = ext.to_lowercase();

        println!("{} {:?}", "Found file:".truecolor(169, 169, 169), file_path);

        if let Some(dir_name) = ext_map.get(&ext) {
            let target_dir = base_path.join(dir_name);

            if !target_dir.exists() {
                fs::create_dir(&target_dir)?;
            }

            fs::rename(&file_path, target_dir.join(entry.file_name()))?;
            println!("{} {:?} {} {:?}", "Moving".bright_magenta(), file_path, "->".bright_magenta(), target_dir);
        }

    }

    println!("{}", "Successfully sorted all your files!".bright_green());

    Ok(())

}


fn encrypt_file(cipher: &ChaCha20Poly1305, path: &Path) -> Result<(), Box<dyn std::error::Error>> {
    let ext = path.extension().and_then(|e| e.to_str()).unwrap_or("");

    if ext == "xyz" || ext == "xyzext" {
        return Ok(());
    }
    
    let data = fs::read(path)?;

    let mut nonce_bytes = [0u8; 12];
    OsRng.fill_bytes(&mut nonce_bytes);

    let nonce = Nonce::from(nonce_bytes);

    let encrypted = cipher.encrypt(&nonce, data.as_ref())
        .map_err(|e| format!("Encrypting error {e}..."))?;

    let mut output = nonce_bytes.to_vec();
    output.extend_from_slice(&encrypted);

    let new_path = path.with_extension("xyz");
    fs::write(&new_path, output)?;

    let ext = path.extension().and_then(|e| e.to_str()).unwrap_or("");
    let ext_path = path.with_extension("xyzext");
    fs::write(&ext_path, ext)?;

    remove_file(path)?;

    println!("{} {:?}", "Encrypted: ".bright_magenta(), new_path);
    Ok(())
}

fn decrypt_file(cipher: &ChaCha20Poly1305, path: &Path) -> Result<(), Box<dyn std::error::Error>> {
    if path.extension().and_then(|e| e.to_str()) != Some("xyz") {
        return Ok(());
    }
    
    let data = fs::read(path)?;

    let (nonce_bytes, encrypted) = data.split_at(12);

    let nonce = Nonce::from_slice(nonce_bytes);

    let decrypted = cipher.decrypt(nonce, encrypted)
        .map_err(|e| format!("Decryption error {e}... Maybe wrong key?"))?;

    let ext_path = path.with_extension("xyzext");
    let ext = fs::read_to_string(&ext_path).unwrap_or("bin".to_string());
    let ext = ext.trim();

    let new_path = path.with_extension(ext);
    fs::write(&new_path, decrypted)?;

    remove_file(path)?;
    remove_file(&ext_path)?;

    println!("{} {:?}", "Decrypted: ".bright_magenta(), new_path);
    Ok(())
}

fn decrypt(path: &Path, cipher: &ChaCha20Poly1305) -> Result<(), Box<dyn std::error::Error>> {
    if path.is_file() {
        decrypt_file(cipher, path)?;
    }
    else if path.is_dir() {
         for entry in fs::read_dir(path)? {
            let entry = entry?;
            let entry_path = entry.path();
            decrypt(&entry_path, cipher)?;
         }
    }

    Ok(())
}

fn encrypt(path: &Path, cipher: &ChaCha20Poly1305) -> Result<(), Box<dyn std::error::Error>> {
    if path.is_file() {
        encrypt_file(cipher, path)?;
    }
    else if path.is_dir() {
         for entry in fs::read_dir(path)? {
            let entry = entry?;
            let entry_path = entry.path();
            encrypt(&entry_path, cipher)?;
         }
    }

    Ok(())
}