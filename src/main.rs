use std::collections::HashMap;
use std::env::current_dir;
use std::fs;
use std::env;
use std::path::PathBuf;
use serde_json::Value;
use colored::*;


fn main() {
    let types_path = "C:/Tools/configurations/properties/properties.types";
    let json_data = get_json(types_path);

    let ext_map = build_extension_map(&json_data);

    let args: Vec<String> = env::args().collect();

    if args.len() > 2 {
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

        println!("{} {:?}", "Found file:".black(), file_path);

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
