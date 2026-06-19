from colorama import Fore, Style
import time

asciiArt = (Fore.LIGHTCYAN_EX + r'''
  /$$$$$$                                                   
 /$$__  $$                                                  
| $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$ 
| $$       |____  $$ /$$__  $$ /$$_____/ |____  $$ /$$__  $$
| $$        /$$$$$$$| $$$$$$$$|  $$$$$$   /$$$$$$$| $$  \__/
| $$    $$ /$$__  $$| $$_____/ \____  $$ /$$__  $$| $$      
|  $$$$$$/|  $$$$$$$|  $$$$$$$ /$$$$$$$/|  $$$$$$$| $$      
 \______/  \_______/ \_______/|_______/  \_______/|__/      '''+ Style.RESET_ALL + '''\n''')

simbol1 = (Fore.LIGHTRED_EX +'''[''')
simbol3 = (Fore.LIGHTRED_EX +''']''')
simbol2 = (Fore.LIGHTYELLOW_EX + '''+''')
simboljadi = (simbol1 + simbol2 + simbol3 + Style.RESET_ALL)
Style.RESET_ALL


symbol2 = (Fore.LIGHTYELLOW_EX + '''1''')

simboll1 = (simbol1 + symbol2 + simbol3 + Style.RESET_ALL)
Style.RESET_ALL

symbol6 = (Fore.LIGHTYELLOW_EX + '''2''')

simboll2 = (simbol1 + symbol6 + simbol3 + Style.RESET_ALL)
Style.RESET_ALL

s1 = (Fore.LIGHTGREEN_EX +'''[''')
s2 = (Fore.LIGHTGREEN_EX +''']''')
s3 = (Fore.LIGHTBLUE_EX + '''+''')

simbolSuces = (s1  + s3 + s2 + Style.RESET_ALL)
Style.RESET_ALL