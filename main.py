import os
import sys
import time
import subprocess
from theme import set_theme, get_current_theme, themes
from pystyle import Colors, Colorate, Write

def animated_text(text, delay=0.05):
    for line in text.split('\n'):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write('\n')
        sys.stdout.flush()
        time.sleep(delay)

def display_ascii_art():
    current_theme = get_current_theme()
    art = f"""{current_theme["primary"]}
 _____     ______     ______     __  __     __   __     ______     ______     ______    
/\  __-.  /\  __ \   /\  == \   /\ \/ /    /\ "-.\ \   /\  ___\   /\  ___\   /\  ___\   
\ \ \/\ \ \ \  __ \  \ \  __<   \ \  _"-.  \ \ \-.  \  \ \  __\   \ \___  \  \ \___  \  
 \ \____-  \ \_\ \_\  \ \_\ \_\  \ \_\ \_\  \ \_\\"\_\  \ \_____\  \/\_____\  \/\_____\ 
  \/____/   \/_/\/_/   \/_/ /_/   \/_/\/_/   \/_/ \/_/   \/_____/   \/_____/   \/_____/ 
                                                                                        

Dev : Atom Tools
───────────────────── 
Version : 2.1
─────────────────────

{current_theme["reset"]}{current_theme["primary"]}1{current_theme["reset"]} Account Nuker               {current_theme["primary"]}11{current_theme["reset"]} Ip Information                  {current_theme["primary"]}21{current_theme["reset"]} Number Scrapper    
{current_theme["primary"]}2{current_theme["reset"]} Badge Changer               {current_theme["primary"]}12{current_theme["reset"]} Email Information               {current_theme["primary"]}22{current_theme["reset"]} Website Scrapper    
{current_theme["primary"]}3{current_theme["reset"]} Clear Dm                    {current_theme["primary"]}13{current_theme["reset"]} Number Information              {current_theme["primary"]}23{current_theme["reset"]} IBAN Generator      
{current_theme["primary"]}4{current_theme["reset"]} Group Spammer               {current_theme["primary"]}14{current_theme["reset"]} Get your Ip                     {current_theme["primary"]}24{current_theme["reset"]} CC Generator        
{current_theme["primary"]}5{current_theme["reset"]} Server Info                 {current_theme["primary"]}15{current_theme["reset"]} Roblox Id Information           {current_theme["primary"]}25{current_theme["reset"]} Obfuscator          
{current_theme["primary"]}6{current_theme["reset"]} Status Rotator              {current_theme["primary"]}16{current_theme["reset"]} Token Information               {current_theme["primary"]}26{current_theme["reset"]} Token Generator     
{current_theme["primary"]}7{current_theme["reset"]} Token Checker               {current_theme["primary"]}17{current_theme["reset"]} Roblox User Information         {current_theme["primary"]}27{current_theme["reset"]} Dos Voice           
{current_theme["primary"]}8{current_theme["reset"]} Token Mass Dm               {current_theme["primary"]}18{current_theme["reset"]} Username Tracker                {current_theme["primary"]}28{current_theme["reset"]} Theme Changer                           
{current_theme["primary"]}9{current_theme["reset"]} Webhook Info                {current_theme["primary"]}19{current_theme["reset"]} Nitro Generator                                          
{current_theme["primary"]}10{current_theme["reset"]} Webhook Spammer            {current_theme["primary"]}20{current_theme["reset"]} Tools Information                                        

{current_theme["reset"]}"""
    animated_text(art, delay=0.01)

def execute_script(script_name):
    script_path = os.path.join('utils', f'{script_name}')
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"{get_current_theme()['primary']}Error executing script '{script_name}': {e}{get_current_theme()['reset']}")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    current_theme = get_current_theme()

    warning_message = f"""
{current_theme["primary"]}
      ____               
     /___/\_     WARNING: The use of these tools can have significant
    _\   \/_/\__  risks and consequences. By using this software, you
  __\       \/_/\  agree that we are not responsible for any damage or
  \   __    __ \ \  issues that may arise from the use of these tools.
 __\  \_\   \_\ \ \   __  Please use responsibly and at your own risk.
/_/\\   __   __  \ \_/_/\          
\_\/_\__\/\__\/\__\/_\_\/          
   \_\/_/\       /_\_\/
      \_\/       \_\/
{current_theme["reset"]}
    """

    animated_text(warning_message, delay=0.03)

    input("\nPress Enter to continue...")

    os.system('cls' if os.name == 'nt' else 'clear')

    display_ascii_art()
    
    while True:
        current_theme = get_current_theme()
        prompt = f"""
{current_theme["primary"]}╭─── {current_theme["secondary"]}atom@user/Multi tools{current_theme["reset"]}
{current_theme["primary"]}│
{current_theme["primary"]}│
{current_theme["primary"]}╰─$ {current_theme["reset"]} """
        option_01 = "Tool-Info"
option_02 = "Tool-Website"
option_03 = "Obfuscator-Tool-(Paid)"
option_04 = "Virus-Build-(Stealer,-Malware)"
option_05 = "Sql-Vulnerability"
option_06 = "Phishing-Attack"
option_07 = "Website-Info-Scanner"
option_08 = "Website-Url-Scanner"
option_09 = "Dark-Web-Links"
option_10 = "Search-In-DataBase"
option_11 = "Dox-Create"
option_12 = "Dox-Tracker-(Osint)"
option_13 = "Username-Tracker-(Osint)"
option_14 = "Email-Tracker-(Osint)"
option_15 = "Email-Info-(Lookup)"
option_16 = "Number-Info-(Lookup)"
option_17 = "Ip-Info-(Lookup)"
option_18 = "Ip-Port-Scanner"
option_19 = "Ip-Pinger"
option_20 = "Ip-Generator"
option_21 = "Password-Encrypted"
option_22 = "Password-Decrypted"
option_23 = "Get-Your-Ip"
option_24 = "Discord-Token-Info"
option_25 = "Discord-Token-Nuker"
option_26 = "Discord-Token-Joiner"
option_27 = "Discord-Token-Leaver"
option_28 = "Discord-Token-Login"
option_29 = "Discord-Token-To-Id-And-Brute"
option_32 = "Discord-Token-Server-Raid"
option_33 = "Discord-Token-Spammer"
option_34 = "Discord-Token-Delete-Friends"
option_35 = "Discord-Token-Block-Friends"
option_36 = "Discord-Token-Mass-Dm"
option_37 = "Discord-Token-Delete-Dm"
option_38 = "Discord-Token-Status-Changer"
option_39 = "Discord-Token-Language-Changer"
option_40 = "Discord-Token-House-Changer"
option_41 = "Discord-Token-Theme-Changer"
option_42 = "Discord-Token-Generator"
option_43 = "Discord-Bot-Server-Nuker"
option_44 = "Discord-Bot-Invite-To-Id"
option_45 = "Discord-Server-Info"
option_46 = "Discord-Nitro-Generator"
option_47 = "Discord-Webhook-Info"
option_48 = "Discord-Webhook-Delete"
option_49 = "Discord-Webhook-Spammer"
option_50 = "Discord-Webhook-Generator"
option_51 = "Roblox-Cookie-Login"
option_52 = "Roblox-Cookie-Info"
option_53 = "Roblox-User-Info"
option_54 = "Roblox-Id-Info"
option_55 = "Soon"
option_56 = "Soon"
option_57 = "Soon"
option_58 = "Soon"
option_59 = "Soon"
option_60 = "Soon"
option_61 = "Soon" 
option_62 = "Soon"
option_63 = "Soon"
option_64 = "Soon"
option_65 = "Soon"
option_66 = "Soon"
option_67 = "Soon"
option_68 = "Soon"
option_69 = "Soon"

option_next = "Next Page >>"
option_previous = "<< Previous Page"
                   print(f"{i}. {theme_name}")
            theme_choice = input("Choose a theme by number: ").strip()
            theme_names = list(themes.keys())
            try:
                theme_index = int(theme_choice) - 1
                if 0 <= theme_index < len(theme_names):
                    set_theme(theme_names[theme_index])
                    os.system('cls' if os.name == 'nt' else 'clear')
                    display_ascii_art() 
                else:
                    print(f"{get_current_theme()['primary']}Invalid choice. No theme changed.{get_current_theme()['reset']}")
            except ValueError:
                print(f"{get_current_theme()['primary']}Invalid input. Please enter a number.{get_current_theme()['reset']}")

if __name__ == "__main__":
    main()

