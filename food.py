foods = ["APPLE", "HONEY"]


class Food:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.frozen = False  # if frozen in shop


class Apple(Food):
    def __init__(self):
        Food.__init__(self, "APPLE", "Give an animal +1/+1.")


class Honey(Food):
    def __init__(self):
        Food.__init__(self, "HONEY", "Give an animal Honey Bee. (Summon a 1/1 Bee after fainting.)")

