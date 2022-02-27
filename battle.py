import colorama
import ntc
import os
import random
import shop
from pet_tiers import tier_1
import time

from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def init_enemy_team_name():
    prefixes = {'Adorable', 'Amazing', 'Awkward', 'Backwards', 'Barbaric', 'Bare', 'Bearded', 'Blatant', 'Boring',
                'Bumbling', 'Burbling', 'Cartoony', 'Cheesy', 'Chunky', 'Clumsy', 'Comedic', 'Confused', 'Creamy',
                'Crisp', 'Crispified', 'Crunchy', 'Danish', 'Delicious', 'Desolate', 'Desperate', 'Domesticated',
                'Dry', 'Extra', 'Fatherly', 'Fictive', 'Fishy', 'Flooded', 'Flopping', 'Foamy', 'Friendly', 'Frigid',
                'Fussy', 'Gasping', 'Glistering', 'Gushing', 'HUUUGE', 'Hard', 'Helpless', 'Hilly', 'Hot', 'Hungry',
                'Iconic', 'Illegal', 'Improper', 'Inedible', 'Innocent', 'Insolent', 'Jovial', 'Lazy', 'Leaking',
                'Loose', 'Lush', 'Magical', 'Miffed', 'Milky', 'Misty', 'Moist', 'Moody', 'Motherly', 'Nasty',
                'Nefarious', 'Obese', 'Offensive', 'Overpowered', 'Overt', 'Panicking', 'Peculiar', 'Pouting',
                'Precious', 'Proper', 'Rolling', 'Rude', 'Running', 'Salty', 'Shiny', 'Skilled', 'Skulking', 'Slippery',
                'Smooth', 'Sniffing', 'Soft', 'Sour', 'Squeaky', 'Sticky', 'Stormy', 'Suave', 'Submissive', 'Subtle',
                'Sulking', 'Suspicious', 'Talkative', 'Tropical', 'Underwhelming', 'Unintended', 'Unsubtle',
                'Untouched', 'Unwashed', 'Upset', 'Vague', 'Vivid', 'Warmish', 'Wavy', 'Wet', 'Willing', 'Withering',
                'Witty'}
    nouns = {'Abs', 'Arms', 'Aunties', 'Bagels', 'Bagpipes', 'Baguettes', 'Balls', 'Bamboos', 'Bananas', 'Beavers',
             'Belltowers', 'Bits', 'Bones', 'Bosses', 'Bushes', 'Buttocks', 'Cakes', 'Carrots', 'Chipmunks', 'Chunks',
             'Citizens', 'Clementines', 'Craters', 'Cucumbers', 'Doggies', 'Dustbunnies', 'Ears', 'Eggplants',
             'Eruptions', 'Eyes', 'Fanboys', 'Fangirls', 'Feet', 'Fingers', 'Firemen', 'Fishes', 'Fossils', 'Fusspots',
             'Geeks', 'Gems', 'Geysers', 'Glasses', 'Hats', 'Heads', 'Hedges', 'Herbs', 'Hipsters', 'Housewives',
             'Husbands', 'Icecubes', 'Kilts', 'Lawnmowers', 'Masseuses', 'Minerals', 'Monks', 'Mouths', 'Muffins',
             'Mushrooms', 'Noses', 'Nuts', 'Organisms', 'Packages', 'Pants', 'Pearls', 'Pieces', 'Ponies', 'Posers',
             'Presidents', 'Pronks', 'Puppies', 'Rangers', 'Riders', 'Rodents', 'Sailors', 'Sardines', 'Sausages',
             'Scallywags', 'Scouts', 'Shovels', 'Soup', 'Streamers', 'Submarines', 'Swimmers', 'Teabags', 'Teapots',
             'Tentacles', 'Truckers', 'Tugboat', 'Turtles', 'Underdogs', 'Warriors', 'Wigs'}

    prefixes_list = list(prefixes)
    nouns_list = list(nouns)

    enemy_team_name = f"The {prefixes_list[random.randrange(0, len(prefixes_list))]} " \
                      f"{nouns_list[random.randrange(0, len(nouns_list))]}"
    return enemy_team_name


enemy_team = []  # pets in enemy team


def status_battle(pet, j, side="none"):  # prints pet's attributes, same as 'status'

    if side == "team":
        colour = Fore.BLUE  # colour to display pet name
    elif side == "enemy":
        colour = Fore.LIGHTGREEN_EX
    else:
        colour = Fore.CYAN

    if not pet.effect:  # if pet has no effect
        if pet.atk_mod and not pet.hp_mod:  # if pet has attack boost but not hp boost
            print(f"{Style.BRIGHT}{Fore.YELLOW}{j} {colour}{pet.name}{Style.RESET_ALL} : {Fore.RED}{Style.BRIGHT}"
                  f"ATK {Fore.RESET}{pet.attack}*{Style.RESET_ALL}, {Fore.RED}{Style.BRIGHT}HP {Fore.RESET}"
                  f"{pet.health}{Style.RESET_ALL}. {pet.description}")
        elif pet.hp_mod and not pet.atk_mod:  # if pet has hp boost but not attack boost
            print(f"{Style.BRIGHT}{Fore.YELLOW}{j} {colour}{pet.name}{Style.RESET_ALL} : {Fore.RED}{Style.BRIGHT}"
                  f"ATK {Fore.RESET}{pet.attack}{Style.RESET_ALL}, {Fore.RED}{Style.BRIGHT}HP {Fore.RESET}"
                  f"{pet.health}*{Style.RESET_ALL}. {pet.description}")
        elif pet.hp_mod and pet.atk_mod:  # if pet has hp boost and attack boost
            print(f"{Style.BRIGHT}{Fore.YELLOW}{j} {colour}{pet.name}{Style.RESET_ALL} : {Fore.RED}{Style.BRIGHT}"
                  f"ATK {Fore.RESET}{pet.attack}*{Style.RESET_ALL}, {Fore.RED}{Style.BRIGHT}HP {Fore.RESET}"
                  f"{pet.health}*{Style.RESET_ALL}. {pet.description}")
        else:  # if no stat boosts
            print(f"{Style.BRIGHT}{Fore.YELLOW}{j} {colour}{pet.name}{Style.RESET_ALL} : {Fore.RED}{Style.BRIGHT}"
                  f"ATK {Fore.RESET}{pet.attack}{Style.RESET_ALL}, {Fore.RED}{Style.BRIGHT}HP {Fore.RESET}"
                  f"{pet.health}{Style.RESET_ALL}. {pet.description}")

    else:  # if pet has an effect
        if pet.atk_mod and not pet.hp_mod:  # if pet has attack boost but not hp boost
            print(f"{Style.BRIGHT}{Fore.YELLOW}{j} {colour}{pet.name}{Style.RESET_ALL} : {Fore.RED}{Style.BRIGHT}"
                  f"ATK {Fore.RESET}{pet.attack}*{Style.RESET_ALL}, {Fore.RED}{Style.BRIGHT}HP {Fore.RESET}"
                  f"{pet.health}{Style.RESET_ALL}. {pet.description} {Style.BRIGHT}Effect: {Fore.YELLOW}{pet.effect}")
        elif pet.hp_mod and not pet.atk_mod:  # if pet has hp boost but not attack boost
            print(f"{Style.BRIGHT}{Fore.YELLOW}{j} {colour}{pet.name}{Style.RESET_ALL} : {Fore.RED}{Style.BRIGHT}"
                  f"ATK {Fore.RESET}{pet.attack}{Style.RESET_ALL}, {Fore.RED}{Style.BRIGHT}HP {Fore.RESET}"
                  f"{pet.health}*{Style.RESET_ALL}. {pet.description} {Style.BRIGHT}Effect: {Fore.YELLOW}{pet.effect}")
        elif pet.hp_mod and pet.atk_mod:  # if pet has hp boost and attack boost
            print(f"{Style.BRIGHT}{Fore.YELLOW}{j} {colour}{pet.name}{Style.RESET_ALL} : {Fore.RED}{Style.BRIGHT}"
                  f"ATK {Fore.RESET}{pet.attack}*{Style.RESET_ALL}, {Fore.RED}{Style.BRIGHT}HP {Fore.RESET}"
                  f"{pet.health}*{Style.RESET_ALL}. {pet.description} {Style.BRIGHT}Effect: {Fore.YELLOW}{pet.effect}")
        else:  # if no stat boosts
            print(f"{Style.BRIGHT}{Fore.YELLOW}{j} {colour}{pet.name}{Style.RESET_ALL} : {Fore.RED}{Style.BRIGHT}"
                  f"ATK {Fore.RESET}{pet.attack}{Style.RESET_ALL}, {Fore.RED}{Style.BRIGHT}HP {Fore.RESET}"
                  f"{pet.health}{Style.RESET_ALL}. {pet.description} {Style.BRIGHT}Effect: {Fore.YELLOW}{pet.effect}")


def print_team_battle():
    j = 0
    if shop.team:  # if there are pets in your team
        for i in shop.team:
            status_battle(i, j)
            j += 1
    else:
        print("<empty>")


def init_enemy_team(team_name):

    enemy_team_name = init_enemy_team_name()

    save_file = open("save_data/enemy_team_name.txt", "w")
    save_file.write(enemy_team_name)  # save enemy team name in 'enemy_team_name.txt'
    save_file.close()

    number_of_pets = int()  # number of pets generated in enemy team

    if shop.turn == 1:
        number_of_pets = 3
    elif shop.turn == 2:
        number_of_pets = random.choices([4, 5], weights=[2, 8])[0]
    elif shop.turn > 2:
        number_of_pets = 5

    for i in range(number_of_pets):
        enemy_team.append(random.choice(tier_1.pets))  # appends name strings to 'enemy_team'

    enemy_team_classes = ntc.name_to_class(enemy_team)   # converts the name strings to classes
    enemy_team.clear()  # clears the names from the 'enemy_team' list...
    for i in range(number_of_pets):  # so we can add the classes instead
        enemy_team.append(enemy_team_classes[i])  # 'team' should be a list of classes
        enemy_team[i].level = 1  # have to init level for some pet functions

    print(f"{Fore.BLACK}{Back.BLUE}{Style.BRIGHT}«{team_name.upper()}»{Style.RESET_ALL} (you)")
    print_team_battle()

    time.sleep(1)

    # for i in range(0, 3):
    #     loading = f"{Style.BRIGHT}You are fighting against" + "." * i
    #     print(loading, end="\r")
    #     time.sleep(0.5)

    print(f"\nYou are fighting against...")
    time.sleep(1)
    print(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}{enemy_team_name}{Fore.RESET}!\n")

    print(f"{Fore.BLACK}{Back.LIGHTGREEN_EX}{Style.BRIGHT}«{enemy_team_name.upper()}»")  # enemy team name header
    j = 0
    for i in enemy_team_classes:
        status_battle(i, j)
        j += 1


def get_speed():
    speed = float()
    time.sleep(1)

    while not speed:
        battle_speed = input("\nHow fast do you want the battle to be? Enter 'n' for normal and 'f' for fast. ")
        if battle_speed == "n" or battle_speed == "N":
            speed = 1.0
        elif battle_speed == "f" or battle_speed == "F":
            speed = 0.5
        else:
            print("Invalid input.")
    time.sleep(0.5)
    print("")
    print(f"Your pets will have {Fore.BLUE}blue{Fore.RESET} names and the enemy's will have {Fore.LIGHTGREEN_EX}green"
          f"{Fore.RESET} names.\n")
    time.sleep(0.5)
    stepthru = False

    enter = input("Do you want to use the enter key to step through the battle? Enter 'y' for yes or 'n' for no: ")
    while enter != "y" and enter != "Y" and enter != "n" and enter != "N":
        enter = input("Invalid input. Enter 'y' for yes or 'n' for no: ")

    if enter == "y" or enter == "Y":
        stepthru = True

    input(f"\n{Style.BRIGHT}Press enter to start the battle! ")

    return speed, stepthru


def print_both_teams(team_name, enemy_team_name):
    print(f"{Fore.BLACK}{Back.BLUE}{Style.BRIGHT}«{team_name.upper()}»{Style.RESET_ALL} (you)")  # header

    death_count = 0  # number of dead pets in 'team'

    for i in shop.team:  # if a pet in 'team' is dead then add 1 to 'death_count'
        if i.health <= 0:
            death_count += 1

    if death_count != len(shop.team):  # if not all pets are dead
        for i in range(len(shop.team)):  # displays pet status if alive
            if shop.team[i].health <= 0:
                continue
            else:
                status_battle(shop.team[i], i)
            i += 1
    else:
        print("<empty>")

    print("")

    print(f"{Fore.BLACK}{Back.LIGHTGREEN_EX}{Style.BRIGHT}«{enemy_team_name.upper()}»")  # header

    enemy_death_count = 0  # number of dead pets in 'enemy_team'

    for i in enemy_team:  # if a pet in 'team' is dead then add 1 to 'death_count'
        if i.health <= 0:
            enemy_death_count += 1

    if enemy_death_count != len(enemy_team):  # if not all pets are dead
        for i in range(len(enemy_team)):  # displays pet status if alive
            if enemy_team[i].health <= 0:
                continue
            else:
                status_battle(enemy_team[i], i)
            i += 1
    else:
        print("<empty>")

    print("")


def battle_start():

    speed, stepthru = get_speed()
    game_over = False

    os.system('cls')

    orig_team = []  # team before battle
    orig_team_attack = []  # attack of team pets before battle
    orig_team_health = []  # health of team pets before battle

    for i in shop.team:
        orig_team.append(i)
        orig_team_attack.append(i.attack)
        orig_team_health.append(i.health)

    tn_file = open("save_data/team_name.txt")  # team name is stored in 'team_name.txt', 'tn' is short for 'team name'
    team_name = tn_file.readline().strip()  # team name is stored in first line ('strip' removes any line breaks)
    tn_file.close()

    etn_file = open("save_data/enemy_team_name.txt")  # enemy team name is stored in 'enemy_team_name.txt'
    enemy_team_name = etn_file.readline().strip()  # enemy team name is stored in first line

    # initialising counters
    p = 0  # 'p' for 'player'
    b = 0  # 'e' for 'bot', these counters track the index of the current fighting pet

    a = 0  # attack count, how many attacks have been made

    while not game_over:
        print(f"{Fore.BLUE}{Style.BRIGHT}PET {p}/{len(shop.team) - 1} {Fore.WHITE}VS {Fore.LIGHTGREEN_EX}PET {b}/"
              f"{len(enemy_team) - 1}\n")
        if shop.team:  # if team not empty
            print_both_teams(team_name, enemy_team_name)
            if a == 0:  # at start of battle before first pet attacks, check for mosquitoes in both teams
                p, b, mosquito_check = tier_1.mosquito_check(p, b, stepthru, speed)
                if mosquito_check:
                    os.system('cls')
                print(f"{Fore.BLUE}{Style.BRIGHT}PET {p}/{len(shop.team) - 1} {Fore.WHITE}VS {Fore.LIGHTGREEN_EX}PET "
                      f"{b}/{len(enemy_team) - 1}\n")
                print_both_teams(team_name, enemy_team_name)
                a += 1

            if len(shop.team) == 1 and shop.team[0].dead:
                # if only one pet in team and they die from initial mosquito attack for example
                print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}««DEFEAT!»»\n")  # you lose!
                shop.lives -= 1
                for i in range(b, len(enemy_team)):  # prints surviving pets and their statuses
                    enemy_team[i].battle_status(p, b, side="enemy")
                    b += 1
                break
            else:
                if p > len(shop.team):
                    p -= 1
                if b > len(enemy_team):
                    b -= 1

                shop.team[p].attacks(p, b, enemy_team[b], speed)  # attack move

            time.sleep(speed)
            if stepthru:
                input("\nPress enter to continue.")
            os.system('cls')

            if shop.team[p].dead and not enemy_team[b].dead:  # if your pet dies and enemy's doesn't
                p += 1
                a += 1  # increment attack count
            elif enemy_team[b].dead and not shop.team[p].dead:  # if enemy's pet dies and yours doesn't
                b += 1
                a += 1  # increment attack count
            elif not shop.team[p].dead and not enemy_team[b].dead and not shop.team[p].both_dead:  # if no pet dies
                a += 1  # increment attack count
            elif shop.team[p].both_dead:  # if both pets die
                p += 1
                b += 1
                a += 1  # increment attack count

            # BATTLE OUTCOMES #

            if p == len(shop.team) and b != len(enemy_team):  # if all of your pets are dead but some enemy pets are
                # still alive
                print_both_teams(team_name, enemy_team_name)
                print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}««DEFEAT!»»\n")  # you lose!
                shop.lives -= 1
                for i in range(b, len(enemy_team)):  # prints surviving pets and their statuses
                    if not enemy_team[i].dead:
                        enemy_team[i].battle_status(p, b, side="enemy")
                    b += 1
                game_over = True

            elif b == len(enemy_team) and p != len(shop.team):  # if all enemy pets are dead but some of yours are still
                # alive
                print_both_teams(team_name, enemy_team_name)
                print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}««VICTORY!»»\n")  # you win!
                shop.wins += 1
                for i in range(p, len(shop.team)):  # prints surviving pets and their statuses
                    if not shop.team[i].dead:
                        shop.team[p].battle_status(p, b, side="team")
                    p += 1
                game_over = True

            elif p == len(shop.team) and b == len(enemy_team):  # if all pets are dead
                print_both_teams(team_name, enemy_team_name)
                print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}««DRAW!»»")  # no one wins!
                game_over = True

            if p < len(shop.team):  # if a pet in your team is dead, but they are not the pet in front
                while shop.team[p].dead:  # then skip over the pet when it is their turn to fight
                    p += 1  # (for deaths from initial mosquito attack, for example)
                    if p == len(shop.team):
                        break
            if b < len(enemy_team):  # same code but for enemy team
                while enemy_team[b].dead:
                    b += 1
                    if b == len(enemy_team):
                        break

        else:  # if 'team' is empty at start of battle then automatic defeat
            print_both_teams(team_name, enemy_team_name)
            print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}««DEFEAT!»»\n")  # you lose!
            shop.lives -= 1
            for i in range(b, len(enemy_team)):  # prints surviving pets and their statuses
                enemy_team[i].battle_status(p, b, side="enemy")
                b += 1
            game_over = True

    shop.team.clear()  # clears team statuses after battle
    reset_statuses(orig_team, orig_team_attack, orig_team_health)


def reset_statuses(orig_team, orig_team_attack, orig_team_health):  # reverts pet statuses to statuses before battle
    for i in range(len(orig_team)):
        shop.team.append(orig_team[i])
        if shop.team[i].horse_atk_boost:  # take away temporary attack boost from horse ability
            shop.team[i].attack = orig_team_attack[i] - shop.team[i].horse_atk_boost
            shop.team[i].horse_atk_boost = 0
        else:
            shop.team[i].attack = orig_team_attack[i]
        shop.team[i].health = orig_team_health[i]
        shop.team[i].dead = False
        shop.team[i].both_dead = False
        shop.team[i].atk_mod = False
        shop.team[i].hp_mod = False

    for i in range(len(enemy_team)):  # reverts enemy pet statuses to false for next battle
        enemy_team[i].dead = False
        enemy_team[i].both_dead = False
        enemy_team[i].atk_mod = False
        enemy_team[i].hp_mod = False


# if __name__ == "__main__":
