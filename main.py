import os
import time
import pathlib
from configurations.define import create_dir

import tkinter as tk
from tkinter import filedialog


sorter_lbl = """
                                                                                                                                                              
                                                                                                                                                              
   SSSSSSSSSSSSSSS                                               tttt                                              WWWWWWWW                           WWWWWWWW
 SS:::::::::::::::S                                           ttt:::t                                              W::::::W                           W::::::W
S:::::SSSSSS::::::S                                           t:::::t                                              W::::::W                           W::::::W
S:::::S     SSSSSSS                                           t:::::t                                              W::::::W                           W::::::W
S:::::S               ooooooooooo   rrrrr   rrrrrrrrr   ttttttt:::::ttttttt        eeeeeeeeeeee    rrrrr   rrrrrrrrrW:::::W           WWWWW           W:::::W 
S:::::S             oo:::::::::::oo r::::rrr:::::::::r  t:::::::::::::::::t      ee::::::::::::ee  r::::rrr:::::::::rW:::::W         W:::::W         W:::::W  
 S::::SSSS         o:::::::::::::::or:::::::::::::::::r t:::::::::::::::::t     e::::::eeeee:::::eer:::::::::::::::::rW:::::W       W:::::::W       W:::::W   
  SS::::::SSSSS    o:::::ooooo:::::orr::::::rrrrr::::::rtttttt:::::::tttttt    e::::::e     e:::::err::::::rrrrr::::::rW:::::W     W:::::::::W     W:::::W    
    SSS::::::::SS  o::::o     o::::o r:::::r     r:::::r      t:::::t          e:::::::eeeee::::::e r:::::r     r:::::r W:::::W   W:::::W:::::W   W:::::W     
       SSSSSS::::S o::::o     o::::o r:::::r     rrrrrrr      t:::::t          e:::::::::::::::::e  r:::::r     rrrrrrr  W:::::W W:::::W W:::::W W:::::W      
            S:::::So::::o     o::::o r:::::r                  t:::::t          e::::::eeeeeeeeeee   r:::::r               W:::::W:::::W   W:::::W:::::W       
            S:::::So::::o     o::::o r:::::r                  t:::::t    tttttte:::::::e            r:::::r                W:::::::::W     W:::::::::W        
SSSSSSS     S:::::So:::::ooooo:::::o r:::::r                  t::::::tttt:::::te::::::::e           r:::::r                 W:::::::W       W:::::::W         
S::::::SSSSSS:::::So:::::::::::::::o r:::::r                  tt::::::::::::::t e::::::::eeeeeeee   r:::::r                  W:::::W         W:::::W          
S:::::::::::::::SS  oo:::::::::::oo  r:::::r                    tt:::::::::::tt  ee:::::::::::::e   r:::::r                   W:::W           W:::W           
 SSSSSSSSSSSSSSS      ooooooooooo    rrrrrrr                      ttttttttttt      eeeeeeeeeeeeee   rrrrrrr                    WWW             WWW            
                                                                                                                                                              
                                                                                                                                                              
                                                                                                                                                              
                                                                                                                                                              
                                                                                                                                                              
                                                                                                                                                              
                                                                                                                                                              """
__version__ = "1.0"


def boot():
    states = ["|", "/", "|", "\\"]
    for r in range(5):
        for i in range(4):
            print(f"Booting program {states[i]}")
            time.sleep(0.5)
            os.system("cls")

    print(f"\n\n{sorter_lbl}")

    print("Hello! You can sort any directory you want with that tool!\n")


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
        command = input(" >> ").lower().strip()

        values_c = command.split(" ")

        if len(values_c) == 0:
            print("Please enter a command.")

        if values_c[0] == "sort":
            if len(values_c) > 1 and values_c[1].startswith("-s="):
                src = values_c[1].split("=")[1]
                create_dir(src)
            else:
                src = choose_directory()    
                create_dir(src)
        elif values_c[0] == "--version":
            print(f"Current version is {__version__}")
        elif values_c[0] == "--author":
            print(f"The creator of the program is Vova_professor.\nhttps://github.com/Vova-Professor")
        else:
            print("[ERROR!]: Enter a valid command!")


if __name__ == '__main__':
    main()