import pathlib
import json
import os
from colorama import Fore, Style

def extract(lang, path: pathlib.Path):
    """Getting file category"""

    read_text = pathlib.Path(".\\configurations\\properties\\properties.types").read_text(encoding="utf-8")
    suffix = pathlib.Path(path).suffix.strip(".")
    data = json.loads(read_text)

    for key, values in data[lang].items():
        if suffix in values:
           return key 
        

def look_dir(path: pathlib.Path):
    """Checking if directory has subdirectories"""

    for file in path.iterdir():
        if file.is_dir():
            while True:
                choice = input(
                    f"WARNING! Found folder '{file}'. Sort elements in it too? (y/n): "
                ).strip().lower()

                if choice in ("y", "n"):
                    return choice == "y"
    return False


def create_dir(path):

    path = pathlib.Path(path)

    if not path.exists():
        print(Fore.RED + f"[ERROR!]: The current path is not exists!\n{path}\n")
        return

    if not path.is_dir():
        print(Fore.RED + f"[ERROR!]: The current path is not a dir! Stopping the program...\n{path}\n")
        return

    path = pathlib.Path(path)
    deep = look_dir(path)

    if deep:
        for file in pathlib.Path(path).rglob("*.*"):
            category = extract("en", file) or "Others"
            direct = path / category
            if not os.path.exists(direct):
                os.mkdir(direct)
                print(Fore.LIGHTBLACK_EX + f"[DEBUG]: {direct} directory has been created!\n")

            os.replace(file, direct / file.name)
        print(Fore.GREEN + Style.BRIGHT + "[DEBUG]: The files has been successfully sorted!\n")
    else:
        for file in pathlib.Path(path).glob("*.*"):
            category = extract("en", file) or "Others"
            direct = path / category
            if not os.path.exists(direct):
                os.mkdir(direct)
                print(Fore.LIGHTBLACK_EX + f"[DEBUG]: {direct} directory has been created!\n")

            os.replace(file, direct / file.name)

        print(Fore.GREEN + Style.BRIGHT + "[DEBUG]: The files has been successfully sorted!\n")

    
def rmfolder_dir(path):
    path = pathlib.Path(path)

    if not path.exists():
        print(Fore.RED + f"[ERROR!]: The current path is not exists!\n{path}\n")
        return

    removed = 0

    for folder in path.iterdir():
        if folder.is_dir():
            rmfolder_dir(folder)

            if not any(folder.iterdir()):
                folder.rmdir()
                removed += 1

    if removed == 0:
        print(Fore.CYAN + "[DEBUG]: Not empty folder.")
    else:
        print(Fore.CYAN + f"[DEBUG]: Successfuly removed {removed} empty folder!")
                 


    