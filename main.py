import battle
import colorama
import os
import shop
import time

from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print("If you can see this message, then the terminal is not being cleared properly.\nMake sure you are using the "
      "correct program version for your operating system, or try using another IDE or run it in Command Prompt.")

try:
    os.mkdir("save_data")
except OSError as error:
    print(error)

os.system('cls')  # clears terminal when running in Command Prompt

print(f"{Fore.GREEN}###################")
print(f"{Style.BRIGHT}{Fore.CYAN}«{Fore.YELLOW}«{Fore.BLUE}SUPER AUTO PETS{Fore.YELLOW}»{Fore.CYAN}»")
print(f"{Fore.GREEN}###################\n")
print("""In Super Auto Pets you build a team from a lovable cast of animals who will fight for you.
They each have unique abilities, so choose wisely who will join your team!\n""")

time.sleep(1)

input(f"{Style.BRIGHT}Press enter to start Arena Mode. ")

game_lost = False


while not game_lost:
    if shop.turn <= 2:
        pet_shop_stock = 3  # number of pets in shop initially, should go up as you level up
    else:
        pet_shop_stock = 4

    shop.pet_shop(pet_shop_stock)
    time.sleep(1)

    if shop.turn == 1:
        team_name = shop.create_team_name()  # create team name

        save_file = open("save_data/team_name.txt", "w")
        save_file.write(team_name)  # save team name in 'team_name.txt'
        save_file.close()

        time.sleep(1)

    os.system('cls')

    battle.init_enemy_team(pet_shop_stock, team_name)

    battle.battle_start()

    shop.turn += 1

    battle.enemy_team.clear()

    input(f"\n{Style.BRIGHT}Press enter to continue. ")

    os.system('cls')

    if shop.lives <= 0:
        game_lost = True
