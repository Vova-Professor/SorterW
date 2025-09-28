from configurations.define import create_dir, rmfolder_dir
from colorama import Fore, Style
import tkinter as tk
from tkinter import filedialog
from configurations.label import boot
import time
import os
import pathlib


__version__ = "1.2"


def choose_directory():
    root = tk.Tk()
    root.withdraw()
    root.title("SorterW"); 
    root.attributes('-topmost', True)
    root.update()
    folder = filedialog.askdirectory(title="SorterW - Choose folder for sort.", parent=root)
    root.destroy()
    return folder


def main():
    boot()
    while True:
        command = input(Fore.WHITE + Style.RESET_ALL + " >> ").lower().strip()

        values_c = command.split(" ")

        if len(values_c) == 0:
            print("Please, enter a command!\n")

        if values_c[0] == "sort":
            if len(values_c) > 1 and values_c[1].startswith("-s="):
                src = " ".join(values_c[1:]).split("=")[1]
                create_dir(src)
            else:
                src = choose_directory()   
                if not src:
                    print(Fore.CYAN + "You haven't selected any folder.\n")
                    continue 

                create_dir(src)
        elif values_c[0] == "conf":
            conf_f = pathlib.Path().cwd() / "configurations" / "properties" / "properties.types"
            print(Style.BRIGHT + Fore.CYAN + "Opening configuration file...\n")
            os.startfile(conf_f)

        elif values_c[0] == "rmempty":
            print("Are you sure you want to remove empty folders? (y/n): ")
            choose = input(" > ").lower().strip()
            if choose == "y":
                if len(values_c) > 1 and values_c[1].startswith("-s="):
                    src = " ".join(values_c[1:]).split("=")[1]
                    rmfolder_dir(src)
                else:
                    src = choose_directory()
                    if not src:
                        print(Fore.CYAN + "You haven't selected any folder.\n")
                        continue
                    
                    rmfolder_dir(src)
            else:
                continue
                
                

            

        elif values_c[0] == "--version":
            print(Style.BRIGHT + f"Current version is {__version__}")

        elif values_c[0] == "--author":
            print(Style.BRIGHT + f"The creator of the program is Vova_professor.\nhttps://github.com/Vova-Professor\n")
        
        elif values_c[0] in ("exit", "quit"):
            print(Style.BRIGHT + "Quitting the program...")
            time.sleep(1.5)
            break

        else:
            print(Fore.RED + Style.BRIGHT + "[ERROR!]: Enter a valid command!\n")


if __name__ == '__main__':
    main()