import random

from pet import *

pets = ["ANT", "BEAVER", "CRICKET", "DUCK", "FISH", "HORSE", "MOSQUITO", "OTTER", "PIG"]


class Ant(Pet):
    def __init__(self):
        Pet.__init__(self, "ANT", 2, 1, "Faint: Give a random friend +2 ATK and +1 HP.")

    def ant_faint(self, team, index, side):
        if index + 1 != len(team):  # if it is not the only remaining pet in the team
            pet_index = random.randrange(len(team))  # random pet from remaining team members

            death_count = 0  # number of dead pets in team

            for i in team:  # count number of dead pets
                if i.health <= 0:
                    death_count += 1

            if death_count <= len(team):  # if still pets alive
                while team[pet_index].health <= 0:  # shouldn't revive dead pets
                    pet_index = random.randrange(len(team))

                rand_pet = team[pet_index]
                rand_pet.attack += 2 * self.level
                rand_pet.health += 1 * self.level

                rand_pet.atk_mod = True
                rand_pet.hp_mod = True

                if side == "team":
                    print(f"{Style.BRIGHT}{Fore.YELLOW}{pet_index} {Fore.BLUE}{rand_pet.name}{Style.RESET_ALL} gained "
                          f"{Style.BRIGHT}2 {Fore.RED}ATK{Style.RESET_ALL} and {Style.BRIGHT}1 {Fore.RED}HP"
                          f"{Style.RESET_ALL}!\n")
                else:
                    print(f"{Style.BRIGHT}{Fore.YELLOW}{pet_index} {Fore.LIGHTGREEN_EX}{rand_pet.name}{Style.RESET_ALL}"
                          f" gained {Style.BRIGHT}2 {Fore.RED}ATK{Style.RESET_ALL} and {Style.BRIGHT}1 {Fore.RED}HP"
                          f"{Style.RESET_ALL}!\n")


class Beaver(Pet):
    def __init__(self):
        Pet.__init__(self, "BEAVER", 2, 2, "Sell: Give 2 random friends +1 HP.")


class Cricket(Pet):
    def __init__(self):
        Pet.__init__(self, "CRICKET", 1, 2, "Faint: Summon a 1/1 Zombie Cricket.")

    def cricket_faint(self, team, index, side):

        bee = False  # if cricket has honey bee effect

        if team[index].effect == "HONEY BEE":  # if cricket has honey bee effect, then zombie cricket AND bee will spawn
            if len(team) < 5:
                team.insert(index + 1, tier_1.Bee())
                horse_ability(team, team[index + 1], index + 1)
                bee = True

        team.pop(index)
        if len(team) < 5:
            team.insert(index, ZombieCricket())
            team[index].attack = self.level
            team[index].health = self.level

            horse_ability(team, team[index], index)

            if side == "team":
                print(f"{Style.BRIGHT}{Fore.YELLOW}{index} {Fore.BLUE}{team[index].name}{Style.RESET_ALL} was added "
                      f"to your team!\n")
            else:
                print(f"{Style.BRIGHT}{Fore.YELLOW}{index} {Fore.LIGHTGREEN_EX}{team[index].name}{Style.RESET_ALL}"
                      f" was added to the enemy team!\n")

        if bee:
            if side == "team":
                print(f"{Style.BRIGHT}{Fore.YELLOW}{index + 1} {Fore.BLUE}BEE{Style.RESET_ALL} was added to your "
                      f"team!\n")
            else:
                print(f"{Style.BRIGHT}{Fore.YELLOW}{index + 1} {Fore.LIGHTGREEN_EX}BEE{Style.RESET_ALL} was added to "
                      f"the enemy team!\n")


class Duck(Pet):
    def __init__(self):
        Pet.__init__(self, "DUCK", 1, 2, "Sell: Give shop pets +1 HP.")


class Fish(Pet):
    def __init__(self):
        Pet.__init__(self, "FISH", 2, 3, "Level-up: Give all friends +1 ATK and +1 HP.")


class Horse(Pet):
    def __init__(self):
        Pet.__init__(self, "HORSE", 2, 1, "Friend summoned: Give it +1 ATK until the end of battle.")


def horse_ability(team, new_pet, index):  # checks for horses in team, if yes then all summoned pets in battle
    # get attack boost

    horse_count = 0  # number of horses in team

    for i in team:
        if i.name == "HORSE":
            horse_count += i.level

    if horse_count > 0:  # horse ability is to add 1 atk to newly bought pet in team
        new_pet.attack += horse_count  # add 1 atk for each horse in team
        new_pet.atk_mod = True
        print(
            f"{Style.BRIGHT}{Fore.YELLOW}{index} {Fore.CYAN}{new_pet.name}{Style.RESET_ALL}"
            f" gained {Style.BRIGHT}{horse_count} {Fore.RED}ATK{Style.RESET_ALL} until the end of "
            f"battle!")


class Mosquito(Pet):
    def __init__(self):
        Pet.__init__(self, "MOSQUITO", 2, 2, "Start of battle: Deal 1 damage to 1 random enemy.")


def mosquito_check(p, b, stepthru, speed=1.0):
    has_mosquito = False
    attacked = []  # list of pets the mosquito has attacked
    en_attacked = []  # list of pets the enemy mosquito has attacked

    for i in range(len(shop.team)):
        if shop.team[i].name == "MOSQUITO":  # if a mosquito is in 'team'
            has_mosquito = True
            if len(battle.enemy_team) >= shop.team[i].level:  # if enough pets for mosquito to attack most
                for j in range(shop.team[i].level):
                    rand_int_1 = random.randrange(len(battle.enemy_team))  # choose random pet on enemy team
                    while battle.enemy_team[rand_int_1].health <= 0 or rand_int_1 in attacked:  # shouldn't attack
                        # already dead pets or those already attacked
                        rand_int_1 = random.randrange(len(battle.enemy_team))
                    attacked.append(rand_int_1)
                    rand_pet_1 = battle.enemy_team[rand_int_1]
                    rand_pet_1.health -= 1  # take away 1 HP
                    print(f"{Fore.YELLOW}{Style.BRIGHT}{i} {Fore.BLUE}MOSQUITO{Style.RESET_ALL} did {Style.BRIGHT}"
                          f"1{Style.RESET_ALL} damage to {Style.BRIGHT}{Fore.YELLOW}{rand_int_1} {Fore.LIGHTGREEN_EX}"
                          f"{rand_pet_1.name}{Style.RESET_ALL}!")
                    time.sleep(speed)
                    if rand_pet_1.health <= 0:  # if enemy's pet dies from your mosquito's opening attack
                        rand_pet_1.dead = True
                        if rand_pet_1.name == "ANT":
                            rand_pet_1.ant_faint(battle.enemy_team, b, side="enemy")
                        if rand_pet_1.name == "CRICKET":
                            rand_pet_1.cricket_faint(battle.enemy_team, rand_int_1, side="enemy")
                            # b -= 1
                            rand_pet_1.dead = False
                        print(
                            f"\n{Back.LIGHTYELLOW_EX}{Fore.LIGHTGREEN_EX}{Style.BRIGHT}{rand_pet_1.name}{Fore.WHITE} "
                            f"died!{Style.RESET_ALL}\n")
                        if rand_int_1 == 0:
                            b += 1
                        time.sleep(speed)

            elif len(battle.enemy_team) < shop.team[i].level:  # if mosquito is able to attack more than number of pets
                # in other team but there is not enough pets in the team
                for j in range(len(battle.enemy_team)):
                    rand_int_1 = random.randrange(shop.team[i].level)  # choose random pet on enemy team
                    while battle.enemy_team[rand_int_1].health <= 0 or rand_int_1 in attacked:  # shouldn't attack
                        # already dead pets or those already attacked
                        rand_int_1 = random.randrange(len(battle.enemy_team))
                    attacked.append(rand_int_1)
                    rand_pet_1 = battle.enemy_team[rand_int_1]
                    rand_pet_1.health -= 1  # take away 1 HP
                    print(f"{Fore.YELLOW}{Style.BRIGHT}{i} {Fore.BLUE}MOSQUITO{Style.RESET_ALL} did {Style.BRIGHT}"
                          f"1{Style.RESET_ALL} damage to {Style.BRIGHT}{Fore.YELLOW}{rand_int_1} {Fore.LIGHTGREEN_EX}"
                          f"{rand_pet_1.name}{Style.RESET_ALL}!")
                    time.sleep(speed)
                    if rand_pet_1.health <= 0:  # if enemy's pet dies from your mosquito's opening attack
                        rand_pet_1.dead = True
                        if rand_pet_1.name == "ANT":
                            rand_pet_1.ant_faint(battle.enemy_team, b, side="enemy")
                        if rand_pet_1.name == "CRICKET":
                            rand_pet_1.cricket_faint(battle.enemy_team, rand_int_1, side="enemy")
                            # b -= 1
                            rand_pet_1.dead = False
                        print(
                            f"\n{Back.LIGHTYELLOW_EX}{Fore.LIGHTGREEN_EX}{Style.BRIGHT}{rand_pet_1.name}{Fore.WHITE} "
                            f"died!{Style.RESET_ALL}\n")
                        if rand_int_1 == 0:
                            b += 1
                        time.sleep(speed)

    for i in range(len(battle.enemy_team)):
        if battle.enemy_team[i].name == "MOSQUITO":  # if a mosquito is in 'enemy_team'
            has_mosquito = True
            if len(shop.team) >= battle.enemy_team[i].level:  # if enough pets for mosquito to attack most
                for j in range(battle.enemy_team[i].level):
                    rand_int_2 = random.randrange(len(shop.team))  # choose random pet on player's team
                    while battle.enemy_team[rand_int_2].health <= 0 or rand_int_2 in en_attacked:  # shouldn't attack
                        # already dead pets or those already attacked
                        rand_int_2 = random.randrange(len(shop.team))
                    en_attacked.append(rand_int_2)
                    rand_pet_2 = battle.enemy_team[rand_int_2]
                    rand_pet_2.health -= 1  # take away 1 HP
                    print(f"{Fore.YELLOW}{Style.BRIGHT}{i} {Fore.LIGHTGREEN_EX}MOSQUITO{Style.RESET_ALL} did "
                          f"{Style.BRIGHT}1{Style.RESET_ALL} damage to {Style.BRIGHT}{Fore.YELLOW}{rand_int_2} "
                          f"{Fore.BLUE}{rand_pet_2.name}{Style.RESET_ALL}!")
                    time.sleep(speed)
                    if rand_pet_2.health <= 0:  # if enemy's pet dies from your mosquito's opening attack
                        rand_pet_2.dead = True
                        if rand_pet_2.name == "ANT":
                            rand_pet_2.ant_faint(shop.team, p, side="team")
                        if rand_pet_2.name == "CRICKET":
                            rand_pet_2.cricket_faint(shop.team, rand_int_2, side="team")
                            # p -= 1
                            rand_pet_2.dead = False
                        print(
                            f"\n{Back.LIGHTRED_EX}{Fore.BLUE}{Style.BRIGHT}{rand_pet_2.name}{Fore.WHITE} died!"
                            f"{Style.RESET_ALL}\n")
                        if rand_int_2 == 0:
                            p += 1
                        time.sleep(speed)

            elif len(shop.team) < battle.enemy_team[i].level:  # if mosquito is able to attack more than number of pets
                # in other team but there is not enough pets in the team
                for j in range(len(shop.team)):
                    rand_int_2 = random.randrange(len(battle.enemy_team[i].level))  # choose random pet on player's team
                    while battle.enemy_team[rand_int_2].health <= 0 or rand_int_2 in en_attacked:  # shouldn't attack
                        # already dead pets or those already attacked
                        rand_int_2 = random.randrange(len(shop.team))
                    en_attacked.append(rand_int_2)
                    rand_pet_2 = battle.enemy_team[rand_int_2]
                    rand_pet_2.health -= 1  # take away 1 HP
                    print(f"{Fore.YELLOW}{Style.BRIGHT}{i} {Fore.LIGHTGREEN_EX}MOSQUITO{Style.RESET_ALL} did "
                          f"{Style.BRIGHT}1{Style.RESET_ALL} damage to {Style.BRIGHT}{Fore.YELLOW}{rand_int_2} "
                          f"{Fore.BLUE}{rand_pet_2.name}{Style.RESET_ALL}!")
                    time.sleep(speed)
                    if rand_pet_2.health <= 0:  # if enemy's pet dies from your mosquito's opening attack
                        rand_pet_2.dead = True
                        if rand_pet_2.name == "ANT":
                            rand_pet_2.ant_faint(shop.team, p, side="team")
                        if rand_pet_2.name == "CRICKET":
                            rand_pet_2.cricket_faint(shop.team, rand_int_2, side="team")
                            # p -= 1
                            rand_pet_2.dead = False
                        print(
                            f"\n{Back.LIGHTRED_EX}{Fore.BLUE}{Style.BRIGHT}{rand_pet_2.name}{Fore.WHITE} died!"
                            f"{Style.RESET_ALL}\n")
                        if rand_int_2 == 0:
                            p += 1
                        time.sleep(speed)

    time.sleep(speed)
    check_done = True
    if has_mosquito:
        if stepthru:
            input("\nPress enter to continue.")
    return p, b, check_done


class Otter(Pet):
    def __init__(self):
        Pet.__init__(self, "OTTER", 1, 2, "Buy: Give a random friend +1 ATK and +1 HP.")


class Pig(Pet):
    def __init__(self):
        Pet.__init__(self, "PIG", 3, 1, "Sell: Gain an extra 1 gold.")


class ZombieCricket(Pet):
    def __init__(self):
        Pet.__init__(self, "ZOMBIE CRICKET", 1, 1, "")


class Bee(Pet):
    def __init__(self):
        Pet.__init__(self, "BEE", 1, 1, "")
