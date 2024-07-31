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

   [Menu n°1]
    [1] Tool Info                      [11] Dox Create                     [21] Password Encrypted
    [2] Tool Website                   [12] Dox Searcher                   [22] Password Decrypted
    [3] More Tool                      [13] Username Osint                 [23] Your IP
    [4] Backdoor Create                [14] Email Searcher                 [24] Token Information
    [5] Sql Injection.                 [15] Email Osint                    [25] Token Nuker
    [6] Phishing URL                   [16] Number Information             [26] Token Joiner
    [7]  Website Info Scanner          [17] Ip Info (Lookup)               [27] Token Leaver
    [8] Website Link Scanner           [18] Ip Port Scanner                [28] Wehbook Spammer
    [9] Dox In Discord                 [19] DDoS IP                        [29] Token to Id
   [10] Search In DataBase             [20] Generate IP                    [30] More Page >                                        

{current_theme["reset"]}"""

    animated_text(art, delay=0.00)



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


{current_theme["reset"]}

    """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠃⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠾⢛⠒⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣶⣄⡈⠓⢄⠠⡀⠀⠀⠀⣄⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣷⠀⠈⠱⡄⠑⣌⠆⠀⠀⡜⢻⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠳⡆⠐⢿⣆⠈⢿⠀⠀⡇⠘⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⡇⠀⠀⠈⢆⠈⠆⢸⠀⠀⢣⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣧⠀⠀⠈⢂⠀⡇⠀⠀⢨⠓⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣦⣤⠖⡏⡸⠀⣀⡴⠋⠀⠈⠢⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠁⣹⣿⣿⣿⣷⣾⠽⠖⠊⢹⣀⠄⠀⠀⠀⠈⢣⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⣇⣰⢫⢻⢉⠉⠀⣿⡆⠀⠀⡸⡏⠀⠀⠀⠀⠀⠀⢇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡇⡇⠈⢸⢸⢸⠀⠀⡇⡇⠀⠀⠁⠻⡄⡠⠂⠀⠀⠀⠘
⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠛⠓⡇⠀⠸⡆⢸⠀⢠⣿⠀⠀⠀⠀⣰⣿⣵⡆⠀⠀⠀⠀
⠈⢻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣦⣀⡇⠀⢧⡇⠀⠀⢺⡟⠀⠀⠀⢰⠉⣰⠟⠊⣠⠂⠀⡸
⠀⠀⢻⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢧⡙⠺⠿⡇⠀⠘⠇⠀⠀⢸⣧⠀⠀⢠⠃⣾⣌⠉⠩⠭⠍⣉⡇
⠀⠀⠀⠻⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣋⠀⠈⠀⡳⣧⠀⠀⠀⠀⠀⢸⡏⠀⠀⡞⢰⠉⠉⠉⠉⠉⠓⢻⠃
⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣀⠠⠤⣤⣤⠤⠞⠓⢠⠈⡆⠀⢣⣸⣾⠆⠀⠀⠀⠀⠀⢀⣀⡼⠁⡿⠈⣉⣉⣒⡒⠢⡼⠀
⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣎⣽⣶⣤⡶⢋⣤⠃⣠⡦⢀⡼⢦⣾⡤⠚⣟⣁⣀⣀⣀⣀⠀⣀⣈⣀⣠⣾⣅⠀⠑⠂⠤⠌⣩⡇⠀
⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⣺⢁⣞⣉⡴⠟⡀⠀⠀⠀⠁⠸⡅⠀⠈⢷⠈⠏⠙⠀⢹⡛⠀⢉⠀⠀⠀⣀⣀⣼⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡟⢡⠖⣡⡴⠂⣀⣀⣀⣰⣁⣀⣀⣸⠀⠀⠀⠀⠈⠁⠀⠀⠈⠀⣠⠜⠋⣠⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⢿⣿⣿⣷⡟⢋⣥⣖⣉⠀⠈⢁⡀⠤⠚⠿⣷⡦⢀⣠⣀⠢⣄⣀⡠⠔⠋⠁⠀⣼⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠈⠻⣿⣿⢿⣛⣩⠤⠒⠉⠁⠀⠀⠀⠀⠀⠉⠒⢤⡀⠉⠁⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣤⣤⠴⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⠀⠀⠀⠀⠀⢩⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


    animated_text(warning_message, delay=0.00)



    input("\nPress Enter to continue...")



    os.system('cls' if os.name == 'nt' else 'clear')



    display_ascii_art()

    

    while True:

        current_theme = get_current_theme()

        prompt = f"""

{current_theme["primary"]}╭─── {current_theme["secondary"]}darkness@user/Multi tools{current_theme["reset"]}
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
