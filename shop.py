import colorama
import food
import ntc
import os
import random
from pet_tiers import tier_1
import time


from collections import Counter
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def status(index, pet):  # prints pet's attributes when it is in the shop or team

    level_info = pet_lvl_calc(pet)

    if not pet.effect:  # if pet has no effect
        if pet.frozen:  # if pet is frozen in shop and has no effect
            print(f"{Fore.YELLOW}{Style.BRIGHT}{index} {Fore.CYAN}{pet.name}{Style.RESET_ALL} {level_info}: {Fore.RED}"
                  f"{Style.BRIGHT}ATK {Fore.RESET}{pet.attack}{Style.RESET_ALL}, {Fore.RED}{Style.BRIGHT}HP "
                  f"{Fore.RESET}{pet.health}{Style.RESET_ALL}. {pet.description} {Fore.LIGHTBLUE_EX}{Style.BRIGHT}"
                  f"FROZEN")
        elif pet.atk_mod and not pet.hp_mod:  # if pet has attack boost but not hp boost
            print(f"{Fore.YELLOW}{Style.BRIGHT}{index} {Fore.CYAN}{pet.name}{Style.RESET_ALL} {level_info}: {Fore.RED}"
                  f"{Style.BRIGHT}ATK {Fore.RESET}{pet.attack}*{Style.RESET_ALL}, {Fore.RED}{Style.BRIGHT}HP "
                  f"{Fore.RESET}{pet.health}{Style.RESET_ALL}. {pet.description}")
        elif pet.hp_mod and not pet.atk_mod:  # if pet has hp boost but not attack boost
            print(f"{Fore.YELLOW}{Style.BRIGHT}{index} {Fore.CYAN}{pet.name}{Style.RESET_ALL} {level_info}: {Fore.RED}"
                  f"{Style.BRIGHT}ATK {Fore.RESET}{pet.attack}{Style.RESET_ALL}, {Fore.RED}{Style.BRIGHT}HP "
                  f"{Fore.RESET}{pet.health}*{Style.RESET_ALL}. {pet.description}")
        elif pet.hp_mod and pet.atk_mod:  # if pet has hp boost and attack boost
            print(f"{Fore.YELLOW}{Style.BRIGHT}{index} {Fore.CYAN}{pet.name}{Style.RESET_ALL} {level_info}: {Fore.RED}"
                  f"{Style.BRIGHT}ATK {Fore.RESET}{pet.attack}*{Style.RESET_ALL}, {Fore.RED}{Style.BRIGHT}HP "
                  f"{Fore.RESET}{pet.health}*{Style.RESET_ALL}. {pet.description}")
        else:  # if no stat boosts
            print(f"{Fore.YELLOW}{Style.BRIGHT}{index} {Fore.CYAN}{pet.name}{Style.RESET_ALL} {level_info}: {Fore.RED}"
                  f"{Style.BRIGHT}ATK {Fore.RESET}{pet.attack}{Style.RESET_ALL}, {Fore.RED}{Style.BRIGHT}HP "
                  f"{Fore.RESET}{pet.health}{Style.RESET_ALL}. {pet.description}")

    else:  # if pet has effect
        if pet.frozen:  # if pet is frozen in shop and has effect
            print(f"{Fore.YELLOW}{Style.BRIGHT}{index} {Fore.CYAN}{pet.name}{Style.RESET_ALL} {level_info}: {Fore.RED}"
                  f"{Style.BRIGHT}ATK {Fore.RESET}{pet.attack}{Style.RESET_ALL}, {Fore.RED}{Style.BRIGHT}HP "
                  f"{Fore.RESET}{pet.health}{Style.RESET_ALL}. {pet.description} {Style.BRIGHT}Effect: {Fore.YELLOW}"
                  f"{pet.effect} {Fore.LIGHTBLUE_EX}{Style.BRIGHT}FROZEN")
        elif pet.atk_mod and not pet.hp_mod:  # if pet has attack boost but not hp boost
            print(f"{Fore.YELLOW}{Style.BRIGHT}{index} {Fore.CYAN}{pet.name}{Style.RESET_ALL} {level_info}: {Fore.RED}"
                  f"{Style.BRIGHT}ATK {Fore.RESET}{pet.attack}*{Style.RESET_ALL}, {Fore.RED}{Style.BRIGHT}HP "
                  f"{Fore.RESET}{pet.health}{Style.RESET_ALL}. {pet.description} {Style.BRIGHT}Effect: {Fore.YELLOW}"
                  f"{pet.effect}")
        elif pet.hp_mod and not pet.atk_mod:  # if pet has hp boost but not attack boost
            print(f"{Fore.YELLOW}{Style.BRIGHT}{index} {Fore.CYAN}{pet.name}{Style.RESET_ALL} {level_info}: {Fore.RED}"
                  f"{Style.BRIGHT}ATK {Fore.RESET}{pet.attack}{Style.RESET_ALL}, {Fore.RED}{Style.BRIGHT}HP "
                  f"{Fore.RESET}{pet.health}*{Style.RESET_ALL}. {pet.description} {Style.BRIGHT}Effect: {Fore.YELLOW}"
                  f"{pet.effect}")
        elif pet.hp_mod and pet.atk_mod:  # if pet has hp boost and attack boost
            print(f"{Fore.YELLOW}{Style.BRIGHT}{index} {Fore.CYAN}{pet.name}{Style.RESET_ALL} {level_info}: {Fore.RED}"
                  f"{Style.BRIGHT}ATK {Fore.RESET}{pet.attack}*{Style.RESET_ALL}, {Fore.RED}{Style.BRIGHT}HP "
                  f"{Fore.RESET}{pet.health}*{Style.RESET_ALL}. {pet.description} {Style.BRIGHT}Effect: {Fore.YELLOW}"
                  f"{pet.effect}")
        else:  # if no stat boosts
            print(f"{Fore.YELLOW}{Style.BRIGHT}{index} {Fore.CYAN}{pet.name}{Style.RESET_ALL} {level_info}: {Fore.RED}"
                  f"{Style.BRIGHT}ATK {Fore.RESET}{pet.attack}{Style.RESET_ALL}, {Fore.RED}{Style.BRIGHT}HP "
                  f"{Fore.RESET}{pet.health}{Style.RESET_ALL}. {pet.description} {Style.BRIGHT}Effect: {Fore.YELLOW}"
                  f"{pet.effect}")


def pet_lvl_calc(pet):  # calculates pet level
    level_info = ""
    if pet.level:  # if pet has level (pets in store don't have levels)
        if pet.exp == 0:
            pet.level = 1
            level_info = f"{Fore.LIGHTCYAN_EX}(Lvl {Fore.LIGHTYELLOW_EX}1 {Fore.GREEN}□□{Fore.LIGHTCYAN_EX})" \
                         f"{Style.RESET_ALL} "
        elif pet.exp == 1:
            pet.level = 1
            level_info = f"{Fore.LIGHTCYAN_EX}(Lvl {Fore.LIGHTYELLOW_EX}1 {Fore.GREEN}■□{Fore.LIGHTCYAN_EX})" \
                         f"{Style.RESET_ALL} "
        elif pet.exp == 2:
            pet.level = 2
            level_info = f"{Fore.LIGHTCYAN_EX}(Lvl {Fore.LIGHTYELLOW_EX}2 {Fore.GREEN}□□□{Fore.LIGHTCYAN_EX})" \
                         f"{Style.RESET_ALL} "
        elif pet.exp == 3:
            pet.level = 2
            level_info = f"{Fore.LIGHTCYAN_EX}(Lvl {Fore.LIGHTYELLOW_EX}2 {Fore.GREEN}■□□{Fore.LIGHTCYAN_EX})" \
                         f"{Style.RESET_ALL} "
        elif pet.exp == 4:
            pet.level = 2
            level_info = f"{Fore.LIGHTCYAN_EX}(Lvl {Fore.LIGHTYELLOW_EX}2 {Fore.GREEN}■■□{Fore.LIGHTCYAN_EX})" \
                         f"{Style.RESET_ALL} "
        elif pet.exp == 5:
            pet.level = 3
            level_info = f"{Fore.LIGHTCYAN_EX}(Lvl {Fore.LIGHTYELLOW_EX}3 {Fore.GREEN}■■■{Fore.LIGHTCYAN_EX})" \
                         f"{Style.RESET_ALL} "

    pet_level_descriptions(pet)
    return level_info


def pet_level_descriptions(pet):  # updates pet descriptions as they level up
    if pet.name == "ANT":
        if pet.level == 2:
            pet.description = "Faint: Give a random friend +4 ATK and +2 HP."
        elif pet.level == 3:
            pet.description = "Faint: Give a random friend +6 ATK and +3 HP."
    elif pet.name == "BEAVER":
        if pet.level == 2:
            pet.description = "Sell: Give 2 random friends +2 HP."
        elif pet.level == 3:
            pet.description = "Sell: Give 2 random friends +3 HP."
    elif pet.name == "CRICKET":
        if pet.level == 2:
            pet.description = "Faint: Summon a 2/2 Zombie Cricket."
        elif pet.level == 3:
            pet.description = "Faint: Summon a 3/3 Zombie Cricket."
    elif pet.name == "DUCK":
        if pet.level == 2:
            pet.description = "Sell: Give shop pets +2 HP."
        elif pet.level == 3:
            pet.description = "Sell: Give shop pets +3 HP."
    elif pet.name == "FISH":
        if pet.level == 2:
            pet.description = "Level-up: Give all friends +2 ATK and +2 HP."
    elif pet.name == "HORSE":
        if pet.level == 2:
            pet.description = "Friend summoned: Give it +2 ATK until the end of battle."
        elif pet.level == 3:
            pet.description = "Friend summoned: Give it +3 ATK until the end of battle."
    elif pet.name == "MOSQUITO":
        if pet.level == 2:
            pet.description = "Start of battle: Deal 1 damage to 2 random enemies."
        elif pet.level == 3:
            pet.description = "Start of battle: Deal 1 damage to 3 random enemies."
    elif pet.name == "OTTER":
        if pet.level == 2:
            pet.description = "Buy: Give a random friend +2 ATK and +2 HP."
        elif pet.level == 3:
            pet.description = "Buy: Give a random friend +3 ATK and +3 HP."
    elif pet.name == "PIG":
        if pet.level == 2:
            pet.description = "Sell: Gain 2 gold."
        elif pet.level == 3:
            pet.description = "Sell: Gain 3 gold."


def food_description(index, food):
    if food.frozen:
        print(f"{Fore.YELLOW}{Style.BRIGHT}{index} {Fore.CYAN}{food.name}{Style.RESET_ALL} : {food.description} "
              f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}FROZEN")
    else:
        print(f"{Fore.YELLOW}{Style.BRIGHT}{index} {Fore.CYAN}{food.name}{Style.RESET_ALL} : {food.description}")


def init_pet_shop(pet_shop_stock, frozen_indexes, ps_before, foods_before):  # 'pet_shop_stock' is number of pets
    # available in store at start of round

    if frozen_indexes:  # if there are any pets frozen from before re-roll

        pet_shop = []  # types of pet available in store
        food_names = []  # names of foods available in the store
        pet_numbers = []  # numbers (indexes) of pets available in store
        food_numbers = []  # numbers (indexes) of foods available in store

        for i in range(pet_shop_stock):
            pet_shop.append(random.choice(tier_1.pets))  # adds x number of pets to shop

        pet_shop_classes = ntc.name_to_class(pet_shop)

        for i in range(len(pet_shop_classes)):
            if str(i) in frozen_indexes:  # if current index is in 'frozen_indexes':
                pet_shop_classes.pop(i)  # remove the random pet at index 'i'
                pet_shop_classes.insert(i, ps_before[str(i)])  # 'ps_before' is a dictionary, keys are index number and
                # values are pet class
            pet_numbers.append(str(i))  # adds index of current pet to the list of available index numbers

        for i in range(pet_shop_stock - 2):  # number of foods is (number of pets - 2)
            food_names.append(random.choice(food.foods))  # adds x number of foods to shop

        foods = ntc.f_name_to_class(food_names)

        max_pet_index = 0  # largest pet index value
        for i in pet_numbers:
            if int(i) > max_pet_index:
                max_pet_index = int(i)

        for i in range(len(foods)):
            true_fn_index = int(i) + max_pet_index + 1
            if str(true_fn_index) in frozen_indexes:  # if current index is in 'frozen_indexes':
                foods.pop(i)  # remove the random pet at index 'i'
                foods.insert(i, foods_before[str(i)])  # 'ps_before' is a dictionary, keys are index number and
                # values are pet class
            food_numbers.append(str(i))  # adds index of current food to the list of available index numbers

        true_fn = []  # short for 'true_food_numbers'
        # if 'food_numbers' is [0, 1], 'true_fn' will be [3, 4]

        for i in food_numbers:
            j = int(i) + max_pet_index + 1  # adds largest pet index value to food index so that
            # they don't have same numbers and foods are to be bought in shop
            true_fn.append(str(j))

        return pet_shop_classes, foods, pet_numbers, food_numbers, true_fn

    else:  # if no pets frozen before initialising
        pet_shop = []  # types of pet available in store
        food_names = []  # names of foods available in the store
        pet_numbers = []  # numbers (indexes) of pets available in store
        food_numbers = []  # numbers (indexes) of foods available in store

        for i in range(pet_shop_stock):  # if 'pet_shop_stock' = x
            pet_shop.append(random.choice(tier_1.pets))  # adds x number of pets to shop

        pet_shop_classes = ntc.name_to_class(pet_shop)

        for i in range(len(pet_shop_classes)):
            pet_numbers.append(str(i))  # adds index of current pet to the list of available index numbers

        for i in range(pet_shop_stock - 2):  # number of foods is (number of pets - 2)
            food_names.append(random.choice(food.foods))  # adds x number of foods to shop

        foods = ntc.f_name_to_class(food_names)

        for i in range(len(foods)):
            food_numbers.append(str(i))  # adds index of current food to the list of available index numbers

        max_pet_index = 0  # largest pet index value
        for i in pet_numbers:
            if int(i) > max_pet_index:
                max_pet_index = int(i)

        true_fn = []  # short for 'true_food_numbers'
        # if 'food_numbers' is [0, 1], 'true_fn' will be [3, 4]

        for i in food_numbers:
            j = int(i) + max_pet_index + 1  # adds largest pet index value to food index so that
            # they don't have same numbers and foods are to be bought in shop
            true_fn.append(str(j))

        return pet_shop_classes, foods, pet_numbers, food_numbers, true_fn


def print_shop(pet_numbers, psc, foods, food_numbers, true_fn, gold):
    print(f"{Fore.BLACK}{Back.LIGHTGREEN_EX}{Style.BRIGHT}«PET SHOP»")  # a fancy header for the shop

    if pet_numbers:  # if there are still pets in the shop (if pet shop not empty)
        for i in pet_numbers:
            j = int(i)
            status(j, psc[j])  # prints attributes of pet and its index number in the shop
    else:
        if gold >= 1:
            print("<empty> (Input 'r' to re-roll!)")
        else:
            print("<empty>")

    print(f"\n{Fore.BLACK}{Back.LIGHTGREEN_EX}{Style.BRIGHT}«FOOD SHOP»")

    if food_numbers:  # if there are still foods in the shop (if food shop not empty)
        for i in range(len(food_numbers)):
            j = int(food_numbers[i])
            food_description(true_fn[i], foods[j])  # prints attributes of food and its index number in the shop
    else:
        if gold >= 1:
            print("<empty> (Input 'r' to re-roll!)")
        else:
            print("<empty>")

    print(f"\n{Fore.BLACK}{Back.LIGHTYELLOW_EX}You have {gold} gold.")  # print amount of gold
    print(f"{Fore.BLACK}{Back.WHITE}Buy a pet or food for 3 gold.")
    print(f"{Style.BRIGHT}Enter the number of the pet or food you want to buy or enter 'z' to end your turn.")
    print(f"{Style.BRIGHT}Enter 'a' to reorder the pets in your team.")
    print(f"{Style.BRIGHT}Enter 's' to sell one of your pets.")
    print(f"{Style.BRIGHT}Enter 'd' to merge two pets of the same type.")
    print(f"{Style.BRIGHT}Enter 'f' to freeze or unfreeze a pet or food in the store.")


def print_team():
    print(f"{Fore.BLACK}{Back.BLUE}{Style.BRIGHT}«YOUR TEAM»")
    if team:  # if there are pets in your team
        for i in range(len(team)):
            status(i, team[i])  # print each pet's status
    else:
        print("<empty>")


team = []  # your current team of pets

ps_before = dict()  # pets in shop before re-rolling
foods_before = dict()  # foods in shop before re-rolling
frozen_indexes = []  # list of indexes frozen in the shop which will not be rerolled

turn = 1  # what turn you are on
lives = 10
wins = 0


def pet_shop(pet_shop_stock):
    psc, foods, pet_numbers, food_numbers, true_fn = init_pet_shop(pet_shop_stock, frozen_indexes, ps_before,
                                                                   foods_before)
    # 'psc' is short for 'pet_shop_classes'
    gold = 10  # gold at start of round
    buy_pet = ""  # number of pet you want to buy

    while gold > 0 and buy_pet not in pet_numbers and buy_pet not in pet_numbers or buy_pet != "z" or \
            buy_pet != "Z":  # while you still have gold
        # and the pet or food you want to buy is not available, or turn hasn't ended

        horse_count = 0  # number of horses in team

        for i in team:
            if i.name == "HORSE":
                horse_count += i.level

        os.system('cls')  # clears terminal when running in Command Prompt
        print(f"{Fore.MAGENTA}{Style.BRIGHT}TURN {turn}{Fore.RESET},{Fore.LIGHTMAGENTA_EX} LIVES : {lives}{Fore.RESET},"
              f"{Fore.MAGENTA} WINS : {wins}\n")

        print_team()  # prints your team
        print("")
        print_shop(pet_numbers, psc, foods, food_numbers, true_fn, gold)

        buy_pet = input(f"{Style.BRIGHT}You can also enter 'r' to get new pets in the shop for 1 gold: ")
        print("")

        if buy_pet not in pet_numbers and buy_pet not in true_fn and buy_pet not in "zZrRaAsSgGfFadDxX":  # if the
            # pet or food you want to buy is not available or does not exist, or you don't enter a valid letter for a
            # function
            print("That pet isn't available.")

        ##### BUYING PET #####

        if buy_pet in pet_numbers:  # if pet you are buying is available
            if len(team) >= 5:
                print("You can only have 5 pets in your team. Sell or merge pets to make room for more.")
                input(f"\n{Style.BRIGHT}Press enter to continue. ")
            else:
                gold -= 3
                if gold < 0:
                    gold += 3  # if not enough gold then refund
                    print("Not enough gold.")
                else:  # if enough gold
                    buy_pets(pet_numbers, buy_pet, psc, horse_count)

        ##### BUYING FOOD #####

        if buy_pet in true_fn:  # if you are buying food
            if not team:
                gold += 3  # if not enough gold then refund
                print("You don't have any pets to feed!")
                time.sleep(0.5)
            else:
                gold -= 3
                if gold < 0:
                    gold += 3  # if not enough gold then refund
                    print("Not enough gold.")
                else:  # if enough gold
                    gold = buy_food(gold, true_fn, buy_pet, foods, food_numbers)

        ##### ENDING TURN #####

        elif buy_pet == "z" or buy_pet == "Z":  # if you enter 'z' to end the turn
            if gold > 0:  # if you still have some gold left
                confirm_end = input(f"{Style.BRIGHT}End turn with excess gold? Enter 'y' for yes or any other "
                                    f"character for no: ")
                if confirm_end == "y" or confirm_end == "Y":
                    print("Ended turn.")
                    break
            else:  # if you have no gold left
                confirm_end = input(f"{Style.BRIGHT}End turn? Enter 'y' for yes or any other character for no: ")
                if confirm_end == "y" or confirm_end == "Y":
                    print("Ended turn.")
                    break

        ##### RE-ROLLING PETS #####

        elif buy_pet == "r" or buy_pet == "R":  # if you want to re-roll pets
            gold -= 1
            if gold < 0:
                gold += 1  # if not enough gold then refund
                print("Not enough gold.")
            else:
                ps_before.clear()
                foods_before.clear()
                for i in pet_numbers:  # set 'ps_before' to state of pet shop before re-rolling
                    ps_before.update({i: psc[int(i)]})
                for i in food_numbers:  # set 'foods_before' to state of food shop before re-rolling
                    foods_before.update({i: foods[int(i)]})
                # re-roll
                psc, foods, pet_numbers, food_numbers, true_fn = init_pet_shop(pet_shop_stock, frozen_indexes,
                                                                               ps_before, foods_before)

        ##### RE-ORDERING TEAM #####

        elif buy_pet == "a" or buy_pet == "A":  # if you enter 'a' to reposition pets
            if len(team) >= 2:  # if there are enough pets in 'team' to be repositioned
                reorder_pets()
            else:  # if not enough pets
                print("You don't have enough pets to reorder!")

        ##### SELLING PET #####

        elif buy_pet == "s" or buy_pet == "S":  # if you enter 's' to sell a pet
            if team:
                new_gold = sell_pet(gold, psc)
                gold = new_gold
                input(f"\n{Style.BRIGHT}Press enter to continue. ")
            else:
                print("You don't any pets to sell!")

        ##### MERGING PETS #####

        elif buy_pet == "d" or buy_pet == "D":  # if you enter 'd' to merge two pets
            if not team:
                gold += 3  # if not enough gold then refund
                print("You don't have any pets to merge!")
                time.sleep(0.5)
            else:
                merge_pets()

        ##### FREEZING PET OR FOOD IN SHOP #####

        elif buy_pet == "f" or buy_pet == "F":  # if you enter 'f' to freeze an item in shop
            freeze_pet(pet_numbers, true_fn, psc, foods, pet_shop_stock, food_numbers)

        ##### DEBUG FUNCTIONS #####

        elif buy_pet == "g" or buy_pet == "G":  # add gold, for debug purposes only
            gold += 10

        elif buy_pet == "x" or buy_pet == "X":  # add experience points
            for i in team:
                i.exp += 1

        time.sleep(0.5)

    return team


def buy_pets(pet_numbers, buy_pet, psc, horse_count):

    pet_numbers.remove(buy_pet)  # removes the index of the pet bought from the list 'pet_numbers' so it
    # can't be bought again

    if psc[int(buy_pet)].frozen:  # if pet was frozen in shop
        psc[int(buy_pet)].frozen = False
        frozen_indexes.remove(buy_pet)

    if psc[int(buy_pet)].name == "OTTER":
        psc[int(buy_pet)].level += 1  # set pet level to 1
        if len(team) >= 1:
            rand_int_1 = random.randrange(len(team))
            rand_pet_1 = team[rand_int_1]
            rand_pet_1.attack += 1 * psc[int(buy_pet)].level
            rand_pet_1.health += 1 * psc[int(buy_pet)].level
            print(
                f"{Style.BRIGHT}{Fore.YELLOW}{rand_int_1} {Fore.CYAN}{rand_pet_1.name}{Style.RESET_ALL}"
                f" gained {Style.BRIGHT}{1 * psc[int(buy_pet)].level} {Fore.RED}ATK{Style.RESET_ALL} and {Style.BRIGHT}"
                f"{1 * psc[int(buy_pet)].level} {Fore.RED}HP{Style.RESET_ALL}!")

    team.append(psc[int(buy_pet)])
    psc[int(buy_pet)].level += 1  # set pet level to 1

    if horse_count > 0:  # horse ability is to add 1 atk to newly bought pet in team
        team[-1].attack += horse_count  # add 1 atk for each horse in team
        # 'team' index is -1 because the new pet is appended to the end
        team[-1].horse_atk_boost = horse_count
        team[-1].atk_mod = True
        print(
            f"{Style.BRIGHT}{Fore.YELLOW}{len(team) - 1} {Fore.CYAN}{team[-1].name}{Style.RESET_ALL}"
            f" gained {Style.BRIGHT}{horse_count} {Fore.RED}ATK{Style.RESET_ALL} until the end of "
            f"battle!")


def buy_food(gold, true_fn, buy_pet, foods, food_numbers):

    index_of_food = int()  # we have to find the index of 'buy_pet' because the first index of 'foods'
    # is zero, which cannot be accessed as it is in 'pet_numbers'
    counter = 0
    for i in true_fn:
        if i == buy_pet:  # if the value in 'true_fn' is equal to user input
            index_of_food = counter  # index of 'buy_pet'
            break
        else:
            counter += 1

    team_indexes = []  # list of all team indexes as strings
    for i in range(len(team)):
        team_indexes.append(str(i))

    if foods[index_of_food].name == "APPLE":
        feed_pet = input("Enter the number of the pet you want to feed the apple to, or enter 'c' to "
                         "cancel: ")
        while feed_pet not in team_indexes and feed_pet != "c" and feed_pet != "C":
            print("That pet is not available.")
            feed_pet = input("\nEnter the number of the pet you want to feed the apple to, or enter "
                             "'c' to cancel: ")

        if feed_pet in team_indexes:
            team[int(feed_pet)].attack += 1
            team[int(feed_pet)].health += 1
            food_numbers.pop(index_of_food)  # removes the index of the food bought from the list so it
            # can't be bought again
            true_fn.remove(buy_pet)
        else:  # if cancel
            gold += 3

    if foods[index_of_food].name == "HONEY":
        feed_pet = input("Enter the number of the pet you want to give the honey to, or enter 'c' to "
                         "cancel: ")
        while feed_pet not in team_indexes and feed_pet != "c" and feed_pet != "C":
            print("That pet is not available.")
            feed_pet = input("\nEnter the number of the pet you want to give the honey to, or enter "
                             "'c' to cancel: ")

        if feed_pet in team_indexes:
            team[int(feed_pet)].effect = "HONEY BEE"
            food_numbers.pop(index_of_food)  # removes the index of the food bought from the list so it
            # can't be bought again
            true_fn.remove(buy_pet)
        else:  # if cancel
            gold += 3

    return gold


def reorder_pets():  # reorder pets in team

    os.system('cls')
    print(f"{Fore.MAGENTA}{Style.BRIGHT}TURN {turn}{Fore.RESET},{Fore.LIGHTMAGENTA_EX} LIVES : {lives}{Fore.RESET},"
          f"{Fore.MAGENTA} WINS : {wins}\n")
    print(f"{Fore.BLACK}{Back.BLUE}{Style.BRIGHT}«YOUR TEAM»")

    pet_indexes = []  # list of pet numbers in the team
    for i in range(len(team)):  # adds pet numbers to list 'pet_indexes'
        pet_indexes.append(str(i))

    for j in range(len(team)):
        status(j, team[j])

    cancel = False
    cancel_2 = False

    r_pet = str(input("\nEnter the number of the pet you want to reorder, or enter 'c' to cancel: "))  # short for
    # 'reordered_pet'
    while r_pet not in pet_indexes and r_pet != "c" and r_pet != "C":
        print("That pet is not available.")
        r_pet = str(input("\nEnter the number of the pet you want to reorder, or enter 'c' to cancel: "))

    if r_pet == "c" or r_pet == "C":
        cancel = True

    if not cancel:
        new_pos = input("\nEnter the number of the position you want the pet to have, or enter 'c' to cancel: ")
        # short for 'new_position'
        while new_pos not in pet_indexes and new_pos != "c" and new_pos != "C":
            print("That position is not available.")
            new_pos = input("\nEnter the number of the position you want the pet to have, or enter 'c' to cancel: ")

        if new_pos == "c" or new_pos == "C":
            cancel_2 = True

    if not cancel and not cancel_2:
        r_pet_class = team[int(r_pet)]  # gets the pet to be reordered and stores it in variable 'r_pet_class'
        team.remove(r_pet_class)  # removes the pet to be reordered from the team list

        team.insert(int(new_pos), r_pet_class)  # re-adds the pet into 'team' at its desired position


def sell_pet(new_gold, psc):

    os.system('cls')
    print(f"{Fore.MAGENTA}{Style.BRIGHT}TURN {turn}{Fore.RESET},{Fore.LIGHTMAGENTA_EX} LIVES : {lives}{Fore.RESET},"
          f"{Fore.MAGENTA} WINS : {wins}\n")
    print(f"{Fore.BLACK}{Back.BLUE}{Style.BRIGHT}«YOUR TEAM»")

    pet_indexes = []  # list of pet numbers in the team
    for i in range(len(team)):  # adds pet numbers to list 'pet_indexes'
        pet_indexes.append(str(i))

    for j in range(len(team)):
        status(j, team[j])

    sell = str(input(f"\nEnter the number of the pet you want to sell, or enter 'c' to cancel: "))
    while sell not in pet_indexes and sell != "c" and sell != "C":
        print("That pet is not available.")
        sell = str(input("\nEnter the number of the pet you want to sell, or enter 'c' to cancel: "))

    if sell in pet_indexes:
        spc = team[int(sell)]  # gets the pet to be sold and stores it in variable 'spc'
        # 'spc' is short for 'sell_pet_class'
        team.remove(spc)  # removes sold pet from 'team'

        if spc.name == "PIG":  # if sold pet is a pig
            new_gold += 1  # gain extra gold!
            print(f"{Style.BRIGHT}{Fore.CYAN}PIG{Style.RESET_ALL} sold. You gained {spc.level + 1} gold.")

        elif spc.name == "BEAVER":
            if len(team) > 1:
                rand_int_1 = random.randrange(len(team))
                rand_pet_1 = team[rand_int_1]
                rand_int_2 = random.randrange(len(team))

                while rand_int_2 == rand_int_1:  # 'rand_pet_2' cannot have same value as 'rand_pet_1'
                    rand_int_2 = random.randrange(len(team))

                rand_pet_2 = team[rand_int_2]
                rand_pet_1.health += spc.level
                rand_pet_2.health += spc.level

                print(f"{Style.BRIGHT}{Fore.CYAN}BEAVER{Style.RESET_ALL} sold. You gained {spc.level} gold.")
                print(f"{Style.BRIGHT}{Fore.YELLOW}{rand_int_1} {Fore.CYAN}{rand_pet_1.name}{Style.RESET_ALL} and"
                      f" {Style.BRIGHT}{Fore.YELLOW}{rand_int_2} {Fore.CYAN}{rand_pet_2.name}{Style.RESET_ALL} "
                      f"both gained {Style.BRIGHT}{spc.level} {Fore.RED}HP{Style.RESET_ALL}!")
            elif len(team) == 1:
                for i in range(len(team)):
                    team[i].health += 1
                    print(f"{Style.BRIGHT}{Fore.CYAN}BEAVER{Style.RESET_ALL} sold. You gained {spc.level} gold.")
                    print(f"{Style.BRIGHT}{Fore.YELLOW}{i} {Fore.CYAN}{team[i].name}{Style.RESET_ALL} "
                          f"gained {Style.BRIGHT}{spc.level} {Fore.RED}HP{Style.RESET_ALL}!")
            else:
                print(f"{Style.BRIGHT}{Fore.CYAN}BEAVER{Style.RESET_ALL} sold. You gained {spc.level} gold.")

        elif spc.name == "DUCK":
            for i in psc:
                i.health += spc.level

            print(f"{Style.BRIGHT}{Fore.CYAN}DUCK{Style.RESET_ALL} sold. You gained {spc.level} gold.")
            print(f"All shop pets gained {Style.BRIGHT}{spc.level} {Fore.RED}HP{Style.RESET_ALL}!")

        else:
            print(f"{Style.BRIGHT}{Fore.CYAN}{spc.name}{Style.RESET_ALL} sold. You gained {spc.level} gold.")

        new_gold += spc.level

    return new_gold


def merge_pets():
    team_indexes = []  # list of all team indexes as strings
    for i in range(len(team)):
        team_indexes.append(str(i))
    team_names = []  # list of names of all pets in team
    for i in team:
        team_names.append(i.name)

    counter = (Counter(team_names))
    multiples = []  # list of pets names with multiple occurrences
    for name, occurrences in counter.items():
        if occurrences > 1:
            multiples.append(name)
    if not multiples:
        print("You don't have any pets to merge!")
    else:
        os.system('cls')
        print_team()
        merge = input("\nEnter the number of the pet you want to merge, or enter 'c' to cancel: ")
        print("")
        if merge.isnumeric():  # check if 'merge' is an integer
            if merge in team_indexes:  # if 'merge' is in 'team_indexes'
                if team[int(merge)].exp >= 5:  # check if the pet is already at highest level
                    print("This pet is already at the highest level and cannot merge with another pet.")
                    merge = None  # reset 'merge' so while loop can continue
        while merge not in team_indexes and merge != "c" and merge != "C":
            print("That pet is not available.")
            merge = input("\nEnter the number of the pet you want to merge, or enter 'c' to cancel: ")
            print("")
            if merge.isnumeric():  # check if 'merge' is an integer
                if merge in team_indexes:  # if 'merge' is in 'team_indexes'
                    if team[int(merge)].exp >= 5:  # check if the pet is already at highest level
                        print("This pet is already at the highest level and cannot merge with another pet.")
                        merge = None  # reset 'merge' so while loop can continue

        if merge != "c" and merge != "C":
            status(int(merge), team[int(merge)])  # pet to be merged
            print("")

        if team[int(merge)].name not in multiples:
            print("You don't have any pets to merge!")
            time.sleep(0.5)
        else:
            print("Which pet do you want to merge with? ")
            print("")
            valid_indexes = []  # list of pets available to be merged
            for i in range(len(team)):  # give indexes and statuses of all pets with same name
                if team[i].name == team[int(merge)].name and i != int(merge):
                    status(i, team[i])
                    valid_indexes.append(str(i))

            merge_with = input("\n")
            if merge_with.isnumeric():  # check if 'merge_with' is an integer
                if merge_with in team_indexes:  # if 'merge_with' is in 'team_indexes'
                    if team[int(merge_with)].exp >= 5:  # check if the pet is already at highest level
                        print("This pet is already at the highest level and cannot merge with another pet.")
                        merge_with = None  # reset 'merge_with' so while loop can continue
            while merge_with not in valid_indexes and merge_with != "c" and merge_with != "C":
                print("That pet is not available.")
                merge_with = input("\nEnter the number of the pet you want to merge with, or enter 'c' "
                                   "to cancel: ")
                print("")
                if merge_with.isnumeric():  # check if 'merge_with' is an integer
                    if merge_with in team_indexes:  # if 'merge_with' is in 'team_indexes'
                        if team[int(merge_with)].exp >= 5:  # check if the pet is already at highest level
                            print("This pet is already at the highest level and cannot merge with another pet.")
                            merge_with = None  # reset 'merge_with' so while loop can continue

            if merge_with != "c" and merge_with != "C":
                if team[int(merge)].attack > team[int(merge_with)].attack:  # get larger value of the two pets
                    team[int(merge_with)].attack = team[int(merge)].attack  # and add onto it
                team[int(merge_with)].attack += 1
                if team[int(merge)].health > team[int(merge_with)].health:  # get larger value of the two pets
                    team[int(merge_with)].health = team[int(merge)].health  # and add onto it
                team[int(merge_with)].health += 1
                team[int(merge_with)].exp += team[int(merge)].exp + 1  # add exp of both pets
                if team[int(merge)].effect and not team[int(merge_with)].effect:  # transfer effect
                    team[int(merge_with)].effect = team[int(merge)].effect
                if team[int(merge_with)].name == "FISH":  # if pet is fish
                    if 2 <= team[int(merge_with)].exp < 5:  # if fish has levelled up to level 2
                        for i in range(len(team)):
                            if i == int(merge_with):
                                continue
                            else:
                                team[i].attack += 1
                                team[i].health += 1
                        print(f"All pets in your team gained {Style.BRIGHT}1 {Fore.RED}HP{Style.RESET_ALL}!")
                    elif team[int(merge_with)].exp == 5:  # if fish has levelled up to level 3
                        for i in range(len(team)):
                            if i == int(merge_with):
                                continue
                            else:
                                team[i].attack += 2
                                team[i].health += 2
                        print(f"All pets in your team gained {Style.BRIGHT}2 {Fore.RED}HP{Style.RESET_ALL}!")
                team.pop(int(merge))
                print("Pets merged.")


def freeze_pet(pet_numbers, true_fn, psc, foods, pet_shop_stock, food_numbers):
    frozen = input("Enter the number of the pet or food you want to freeze or unfreeze in the shop, or enter "
                   "'c' to cancel: ")
    while frozen not in pet_numbers and frozen not in true_fn and frozen not in frozen_indexes \
            and frozen != "c" and frozen != "C":
        print("That pet is not available.")
        frozen = input("Enter the number of the pet or food you want to freeze or unfreeze in the shop, or "
                       "enter 'c' to cancel: ")

    if frozen in frozen_indexes:  # unfreeze frozen pet or food
        frozen_indexes.remove(frozen)
        if frozen in pet_numbers:
            psc[int(frozen)].frozen = False
        elif frozen in true_fn:
            foods[int(frozen) - pet_shop_stock - 1].frozen = False

    elif frozen in pet_numbers:
        frozen_indexes.append(frozen)
        psc[int(frozen)].frozen = True
    elif frozen in true_fn:
        frozen_indexes.append(frozen)
        foods[int(frozen) - pet_shop_stock - 1].frozen = True

    ps_before.clear()
    foods_before.clear()
    for i in pet_numbers:  # set 'ps_before' to state of pet shop before re-rolling
        ps_before.update({i: psc[int(i)]})
    for i in food_numbers:  # set 'foods_before' to state of food shop before re-rolling
        foods_before.update({i: foods[int(i)]})


def create_team_name():
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

    prefixes_list = list(prefixes)[:3]
    nouns_list = list(nouns)[:3]
    team_name = ""
    confirm = False

    while not confirm:
        os.system('cls')
        print(f"{Fore.YELLOW}##############")
        print(f"{Fore.GREEN}{Style.BRIGHT}NAME YOUR TEAM")
        print(f"{Fore.YELLOW}##############\n")

        for i in range(3):
            print(f"{Fore.MAGENTA}{Style.BRIGHT}{i}) {Fore.LIGHTCYAN_EX}{prefixes_list[i]}")

        prefix = input(f"\n{Style.BRIGHT}Enter the number of the prefix you want, or enter 3 to auto-generate a team "
                       f"name: ")
        while prefix != "0" and prefix != "1" and prefix != "2" and prefix != "3":
            print(f"{Style.BRIGHT}Invalid input. Must be 0, 1, 2 or 3.")
            prefix = input(f"\n{Style.BRIGHT}Enter the number of the prefix you want: ")
        if prefix == str(3):
            prefix = random.randrange(0, 3)
            noun = random.randrange(0, 3)
            team_name = f"The {prefixes_list[int(prefix)]} {nouns_list[int(noun)]}"
            print(f"\nYour team name is {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{team_name}{Style.RESET_ALL}.")
            break

        print("")
        for i in range(3):
            print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}{i}) {Fore.LIGHTBLUE_EX}{nouns_list[i]}")

        noun = input(f"\n{Style.BRIGHT}Enter the number of the noun you want: ")
        while noun != "0" and noun != "1" and noun != "2":
            print(f"{Style.BRIGHT}Invalid input. Must be 0, 1 or 2.")
            noun = input(f"\n{Style.BRIGHT}Enter the number of the noun you want: ")

        team_name = f"The {prefixes_list[int(prefix)]} {nouns_list[int(noun)]}"

        confirm = input(f"\nYour team name is {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{team_name}{Style.RESET_ALL}. "
                        f"Enter 'y' to confirm or enter any other character to go back. ")
        if confirm == "y" or confirm == "Y":
            confirm = True
        else:
            confirm = False

    return team_name


# if __name__ == "__main__":
