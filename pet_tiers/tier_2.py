import random

from pet import *

pets = ["CRAB", "DODO", "ELEPHANT", "FLAMINGO", "HEDGEHOG", "PEACOCK", "RAT", "SHRIMP", "SPIDER", "SWAN"]


class Crab(Pet):
    def __init__(self):
        Pet.__init__(self, "CRAB", 3, 3, "Buy: Copy Health from the most healthy friend.")


class Dodo(Pet):
    def __init__(self):
        Pet.__init__(self, "DODO", 2, 3, "Start of battle: Give 50% of Dodo's Attack to friend ahead.")


class Elephant(Pet):
    def __init__(self):
        Pet.__init__(self, "ELEPHANT", 3, 5, "Before attack: Deal 1 damage to friend behind.")


class Flamingo(Pet):
    def __init__(self):
        Pet.__init__(self, "FLAMINGO", 3, 1, "Faint: Give the two friends behind +1 ATK and +1 HP.")


class Hedgehog(Pet):
    def __init__(self):
        Pet.__init__(self, "HEDGEHOG", 3, 2, "Faint: Deal 2 damage to all.")


class Peacock(Pet):
    def __init__(self):
        Pet.__init__(self, "PEACOCK", 2, 5, "Hurt: Gain 50% more Attack. Works 1 time per turn.")


class Rat(Pet):
    def __init__(self):
        Pet.__init__(self, "RAT", 4, 5, "Faint: Summon one 1/1 Dirty Rat up front for the opponent.")


class Shrimp(Pet):
    def __init__(self):
        Pet.__init__(self, "SHRIMP", 2, 3, "Friend sold: Give a random friend +1 HP.")


class Spider(Pet):
    def __init__(self):
        Pet.__init__(self, "SPIDER", 2, 2, "Faint: Summon a level 1 tier 3 pet as a 2/2.")


class Swan(Pet):
    def __init__(self):
        Pet.__init__(self, "SWAN", 1, 3, "Start of turn: Gain 1 gold.")
