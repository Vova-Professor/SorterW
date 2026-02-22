# SorterW

Version: v0.1.0

## What is it?
SorterW is an open-source project written in **Rust** that helps you *quickly* sort your files.  
You can configure your own file types using a JSON-based configuration.

Just open `properties.types` and change or add types - it’s simple.

---

## Commands

- Sort your files
```bash
sorterw -sort /path/to/your/folder
```
- Check version
```bash
sorterw --version
```

## ✅ Improvements
- **Rewritten in Rust, speed increased.**


## 🟠 TODO
- Add commands, from previous commit.
- Automatise PATH injection.


## ❗ HOW TO USE IT??
1. Create folder `C:\Tools`
2. Put `sorterw.exe` and `configurations` folder there.
3. Add it to PATH:
    - `WIN + R`

    - `sysdm.cpl`

    - Tab **Advanced**

    - Button **Enviroment Variables**

    - click Edit

    - click New

    - Add:
    ```
    C:\Tools
    ```

    - Click **OK** and restart the _terminal_

    - Check in Terminal 
    ``` Bash
    sorterw --version
    ```