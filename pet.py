import battle
import colorama
import shop
from pet_tiers import tier_1
import time

from colorama import Fore, Back, Style

colorama.init(autoreset=True)


def honey_bee(team, index, side):
    team.pop(index)
    if len(team) < 5:
        team.insert(index, tier_1.Bee())
        tier_1.horse_ability(team, team[index], index)

        if side == "team":
            print(f"{Style.BRIGHT}{Fore.YELLOW}{index} {Fore.BLUE}{team[index].name}{Style.RESET_ALL} was added "
                  f"to your team!\n")
        else:
            print(f"{Style.BRIGHT}{Fore.YELLOW}{index} {Fore.LIGHTGREEN_EX}{team[index].name}{Style.RESET_ALL}"
                  f" was added to the enemy team!\n")

    index += 1


class Pet:
    def __init__(self, name, attack, health, description):
        self.name = name
        self.attack = attack
        self.health = health
        self.description = description

        self.exp = 0  # 2 points is lvl 2, 5 is lvl 3
        self.level = 0  # lvl 1, 2 or 3

        self.effect = str()
        self.frozen = False  # if frozen in shop
        self.horse_atk_boost = 0  # temporary attack boost from horse
        self.atk_mod = False  # if attack values temporarily modified
        self.hp_mod = False  # if health values temporarily modified

        self.dead = False
        self.both_dead = False

    def battle_status(self, p, b, side):  # prints pet's attributes in battle
        if side == "team":
            print(f"{Style.BRIGHT}{Fore.YELLOW}{p} {Fore.BLUE}{self.name}{Style.RESET_ALL} : {Fore.RED}{Style.BRIGHT}"
                  f"ATK {Fore.RESET}{self.attack}{Style.RESET_ALL}, {Fore.RED}{Style.BRIGHT}HP {Fore.RESET}"
                  f"{self.health}{Style.RESET_ALL}.")
        else:
            print(f"{Style.BRIGHT}{Fore.YELLOW}{b} {Fore.LIGHTGREEN_EX}{self.name}{Style.RESET_ALL} : {Fore.RED}"
                  f"{Style.BRIGHT}ATK {Fore.RESET}{self.attack}{Style.RESET_ALL}, {Fore.RED}{Style.BRIGHT}HP "
                  f"{Fore.RESET}{self.health}{Style.RESET_ALL}.")

    def attacks(self, p, b, enemy, speed=1.0):

        # print(battle.enemy_team)  # for some reason this doesn't work when running from 'battle.py' but does work when
        # # running from 'main.py'

        time.sleep(speed)

        # print(f"{Style.BRIGHT}{Fore.YELLOW}{p} {Fore.BLUE}{self.name}{Style.RESET_ALL} attacks {Style.BRIGHT}"
        # f"{Fore.YELLOW}{b} {Fore.LIGHTGREEN_EX}{enemy.name}{Style.RESET_ALL}!")
        enemy.health -= self.attack
        print(f"{Fore.YELLOW}{Style.BRIGHT}{p} {Fore.BLUE}{self.name}{Style.RESET_ALL} did {Style.BRIGHT}{self.attack}"
              f"{Style.RESET_ALL} damage to {Style.BRIGHT}{Fore.YELLOW}{b} {Fore.LIGHTGREEN_EX}{enemy.name}"
              f"{Style.RESET_ALL}!")

        time.sleep(speed)

        # print(f"{Style.BRIGHT}{Fore.YELLOW}{b} {Fore.LIGHTGREEN_EX}{enemy.name}{Style.RESET_ALL} attacks
        # {Fore.YELLOW}"
        # f"{Style.BRIGHT}{p} {Fore.BLUE}{self.name}{Style.RESET_ALL}!")
        self.health -= enemy.attack
        print(f"{Style.BRIGHT}{Fore.YELLOW}{b} {Fore.LIGHTGREEN_EX}{enemy.name}{Style.RESET_ALL} did {Style.BRIGHT}"
              f"{enemy.attack}{Style.RESET_ALL} damage to {Style.BRIGHT}{Fore.YELLOW}{p} {Fore.BLUE}{self.name}"
              f"{Style.RESET_ALL}!")

        print("")

        time.sleep(speed)

        self.battle_status(p, b, side="team")
        enemy.battle_status(p, b, side="enemy")
        print("")

        if enemy.health <= 0 < self.health:  # if enemy died and your pet survived
            enemy.dead = True
            print(f"{Back.LIGHTYELLOW_EX}{Fore.LIGHTGREEN_EX}{Style.BRIGHT}{enemy.name}{Fore.WHITE} died!"
                  f"{Style.RESET_ALL}\n")
            time.sleep(speed)
            if enemy.name == "ANT":
                battle.enemy_team[b].ant_faint(battle.enemy_team, b, side="enemy")
            if enemy.name == "CRICKET":
                battle.enemy_team[b].cricket_faint(battle.enemy_team, b, side="enemy")
                b -= 1
                enemy.dead = False
            if enemy.effect == "HONEY BEE" and enemy.name != "CRICKET":  # if enemy has honey bee effect
                # not cricket because 'cricket_faint' function has honey bee check already
                honey_bee(battle.enemy_team, b, side="enemy")  # spawn bee on death
                b -= 1  # bee takes place of fallen pet
                enemy.dead = False
            return enemy.dead

        elif self.health <= 0 < enemy.health:  # if your pet died and enemy survived
            self.dead = True
            print(f"{Back.LIGHTRED_EX}{Fore.BLUE}{Style.BRIGHT}{self.name}{Fore.WHITE} died!{Style.RESET_ALL}\n")
            time.sleep(speed)
            if self.name == "ANT":
                shop.team[p].ant_faint(shop.team, p, side="team")
            if self.name == "CRICKET":
                shop.team[p].cricket_faint(shop.team, p, side="team")
                p -= 1
                self.dead = False
            if self.effect == "HONEY BEE" and self.name != "CRICKET":  # if player's pet has honey bee effect
                honey_bee(shop.team, p, side="team")  # spawn bee on death
                p -= 1  # bee takes place of fallen pet
                self.dead = False
            return self.dead

        elif enemy.health <= 0 and self.health <= 0:  # if both pets died
            self.both_dead = True
            self.dead = True
            enemy.dead = True
            print(f"{Back.YELLOW}{Fore.WHITE}{Style.BRIGHT}BOTH PETS DIED!{Style.RESET_ALL}\n")
            time.sleep(speed)
            if self.name == "ANT":
                shop.team[p].ant_faint(shop.team, p, side="team")
            if enemy.name == "ANT":
                battle.enemy_team[b].ant_faint(battle.enemy_team, b, side="enemy")
            if self.name == "CRICKET":
                shop.team[p].cricket_faint(shop.team, p, side="team")
                p -= 1
                self.dead = False
                self.both_dead = False
            if self.effect == "HONEY BEE" and self.name != "CRICKET":  # if player's pet has honey bee effect
                honey_bee(shop.team, p, side="team")  # spawn bee on death
                p -= 1  # bee takes place of fallen pet
                self.dead = False
            if enemy.name == "CRICKET":
                battle.enemy_team[b].cricket_faint(battle.enemy_team, b, side="enemy")
                b -= 1
                enemy.dead = False
                self.both_dead = False
            if enemy.effect == "HONEY BEE" and enemy.name != "CRICKET":  # if enemy has honey bee effect
                honey_bee(battle.enemy_team, b, side="enemy")  # spawn bee on death
                b -= 1  # bee takes place of fallen pet
                enemy.dead = False
            return self.both_dead


# if __name__ == "__main__":
