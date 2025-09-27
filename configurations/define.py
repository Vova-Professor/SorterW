import pathlib
import json
import os
from colorama import Fore, Style

def extract(lang, path: pathlib.Path):
    """Getting file category"""
    if not lang in ("en"):
        print(Fore.RED + f"[ERROR!]: The current language is not currently avalible!\n{lang}")

    if not path.exists():
        print(Fore.RED + f"[ERROR!: The current path is not exists!\n{path}")
        return


    read_text = pathlib.Path(".\\configurations\\properties\\properties.types").read_text(encoding="utf-8")
    suffix = pathlib.Path(path).suffix.strip(".")
    data = json.loads(read_text)

    for key, values in data[lang].items():
        if suffix in values:
           return key 
        

def look_dir(path: pathlib.Path):
    """Checking if directory has subdirectories"""

    if not path.exists():
        print(Fore.RED + f"[ERROR!: The current path is not exists!\n{path}")
        return

    if not path.is_dir():
        print(Fore.RED + f"[ERROR!]: The current path is not a dir! Stopping the program...\n{path}")
        return
    
    for file in path.iterdir():
        if file.is_dir():
            while True:
                choice = input(
                    f"WARNING! Found folder '{file}'. Sort elements in it too? (y/n): "
                ).strip().lower()

                if choice in ("y", "n"):
                    return choice == "y"
    return False


def create_dir(path: pathlib.Path):
    path = pathlib.Path(path)
    deep = look_dir(path)

    if not path.exists():
        print(Fore.RED + f"[ERROR!: The current path is not exists!\n{path}")
        return

    if not path.is_dir():
        print(Fore.RED + f"[ERROR!]: The current path is not a dir! Stopping the program...\n{path}")
        return

    if deep:
        for file in pathlib.Path(path).rglob("*.*"):
            category = extract("en", file) or "Others"
            direct = path / category
            if not os.path.exists(direct):
                os.mkdir(direct)
                print(Fore.LIGHTBLACK_EX + f"[DEBUG]: {direct} directory has been created!")

            os.replace(file, direct / file.name)
        print(Fore.GREEN + Style.BRIGHT + "[DEBUG]: The files has been successfully sorted!")
    else:
        for file in pathlib.Path(path).glob("*.*"):
            category = extract("en", file) or "Others"
            direct = path / category
            if not os.path.exists(direct):
                os.mkdir(direct)
                print(Fore.LIGHTBLACK_EX + f"[DEBUG]: {direct} directory has been created!")

            os.replace(file, direct / file.name)

        print(Fore.GREEN + Style.BRIGHT + "[DEBUG]: The files has been successfully sorted!")

    



    