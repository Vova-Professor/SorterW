from colorama import Style
import time
import os


label = """
                                                                                                                                                              
                                                                                                                                                              
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

def boot():
    states = ["|", "/", "|", "\\"]
    for _ in range(5):
        for i in range(4):
            print(Style.BRIGHT + f"Booting the program {states[i]}")
            time.sleep(0.5)
            os.system("cls")

    print(f"{label}\n\n")

    print(Style.RESET_ALL + "Hello! You can sort any directory you want with that tool!\n")
