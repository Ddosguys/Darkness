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
                                                                                        

Dev : KellS
───────────────────── 

Version : 2.1
─────────────────────


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

        

        choice = input(prompt).strip()

        

        if choice == '1':

            execute_script('account_nuker.py')

        elif choice == '2':

            execute_script('badge_changer.py')

        elif choice == '3':

            execute_script('clear_dm.py')

        elif choice == '4':

            execute_script('group_spammer.py')

        elif choice == '5':

            execute_script('server_info.py')

        elif choice == '6':

            execute_script('status_rotator.py')

        elif choice == '7':

            execute_script('token_checker.py')

        elif choice == '8':

            execute_script('token_massdm.py')

        elif choice == '9':

            execute_script('webhook_info.py')

        elif choice == '10':

            execute_script('webhook_spammer.py')

        elif choice == '11':

            execute_script('ip_info.py')

        elif choice == '12':

            execute_script('email_info.py')

        elif choice == '13':

            execute_script('number_info.py')

        elif choice == '14':

            execute_script('get_ip.py')

        elif choice == '15':

            execute_script('roblox_id_info.py')

        elif choice == '16':

            execute_script('token_info.py')

        elif choice == '17':

            execute_script('roblox_user_info.py')

        elif choice == '18':

            execute_script('username_tracker.py')

        elif choice == '19':

            execute_script('nitro_generator.py')

        elif choice == '20':

            execute_script('tools_info.py')

        elif choice == '21':

            execute_script('number_scraper.py')

        elif choice == '22':

            execute_script('website_scraper.py')

        elif choice == '23':

            execute_script('iban_generator.py')

        elif choice == '24':

            execute_script('credit_card_scrapper.py')

        elif choice == '25':

            execute_script('obfuscator.py')

        elif choice == '26':

            execute_script('token_generator.py')

        elif choice == '27':

            execute_script('dos_voice.py')

        elif choice == '28':

            print("\nAvailable themes:")

            for i, theme_name in enumerate(themes.keys(), 1):

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
