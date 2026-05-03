# SorterW

Version: v0.1.2

## What is it?
SorterW is an open-source project written in **Rust** that helps you *quickly* sort your files.  
You can configure your own file types using a JSON-based configuration.

Just open `properties.types` and change or add types - it’s simple.

---


## ❗ HOW TO USE IT??
1. Create folder `C:\Tools`
2. Put `sorterw.exe` and `configurations` folder there.
3. Add it to PATH:
    - `WIN + R`

    - `sysdm.cpl`

    - Tab **Advanced**

    - Button **Environment Variables**

    - Choose Path

    - click Edit

    - click New

    - Add:
    ```
    C:\Tools
    ```

    - Click **OK** and restart the _terminal_

    - Check in Terminal 
    ```bash
    sorterw --version
    ```

## Commands

> [!TIP]
> You can use . if you want to use current directory 

- Sort your files
```bash
sorterw -sort /path/to/your/folder
```

- Remove empty folders
```bash
sorterw -rmempty -dir /path/to/your/folder
```

- Create master key
```bash
sorterw -keygen
```

- Encrypt encrypted file
```bash
sorterw -encrypt /path/to/your/folder/or/file.file KEY
```
(You can use -keygen instead of KEY if you don't have master key yet)

- Decrypt encrypted file
```bash
sorterw -decrypt /path/to/your/folder/or/file.file KEY
```
(You can use -keygen instead of KEY if you don't have master key yet)

- Check version
```bash
sorterw --version
```

## ✅ Improvements
- **Added new commands for encryption!**


## 🟠 TODO
- Add commands, from previous commit.
- Automate PATH injection.