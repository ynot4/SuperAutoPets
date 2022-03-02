foods = ["APPLE", "HONEY"]


class Food:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.frozen = False  # if frozen in shop


class Apple(Food):
    def __init__(self):
        Food.__init__(self, "APPLE", "Give a pet +1 ATK and +1 HP.")


class Honey(Food):
    def __init__(self):
        Food.__init__(self, "HONEY", "Give a pet Honey Bee. (Summon a 1/1 Bee after fainting.)")


class Cupcake(Food):
    def __init__(self):
        Food.__init__(self, "CUPCAKE", "Give a pet +3 ATK and +3 HP until end of battle.")


class MeatBone(Food):
    def __init__(self):
        Food.__init__(self, "MEAT BONE", "Give a pet Bone Attack. (Attack for 5 more damage.)")


class SleepingPill(Food):
    def __init__(self):
        Food.__init__(self, "SLEEPING PILL", "Make a friendly pet faint.")
