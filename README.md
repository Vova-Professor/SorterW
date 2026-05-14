# SorterW

Version: v0.1.3

## What is it?
SorterW is an open-source project written in **Rust** that helps you *quickly* sort your files.  
You can configure your own file types using a JSON-based configuration.

Just open `properties.types` and change or add types - it’s simple.

---


## ❗ HOW TO USE IT??

### Windows
1. Put `sorterw.exe` anywhere, e.g. `C:\Tools`
2. Place `properties.types` at:
```
   C:\Users\<you>\AppData\Roaming\SorterW\properties.types
```
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

### Linux
1. Copy `sorterw` to `/usr/local/bin/`:
```bash
   sudo cp sorterw /usr/local/bin/
```
2. Place `properties.types` at:
```
   ~/.config/SorterW/properties.types
```

### macOS
1. Copy `sorterw` to `/usr/local/bin/`:
```bash
   sudo cp sorterw /usr/local/bin/
```
2. Place `properties.types` at:
```
   ~/Library/Application Support/SorterW/properties.types
```


### Override config path (any OS)
If you want to store the config somewhere else, set an environment variable:
```bash
SORTERW_CONFIG=/your/custom/path/properties.types sorterw -sort .
```

### Now check it
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

- Encrypt file
```bash
sorterw -encrypt /path/to/your/folder/or/file.file KEY
```
(You can use -keygen instead of KEY if you don't have master key yet)

- Decrypt file
```bash
sorterw -decrypt /path/to/your/folder/or/file.file KEY
```
(You can use -keygen instead of KEY if you don't have master key yet)

- Check version
```bash
sorterw --version
```

## ✅ Improvements
- Cross-platform support: Windows, Linux, macOS.


## 🟠 TODO
- Add commands, from previous commit.
- Automate PATH injection.