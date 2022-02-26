from pet_tiers.tier_1 import *
from food import *


# 'ntc' is short for 'name_to_class_converter'

def name_to_class(names):  # 'names' is list of string values of names of pet types
    classes = []  # same as 'names' but all string values are converted to the corresponding pet class

    for i in names:  # matching each string value to its class
        if i == "ANT":
            classes.append(Ant())
        elif i == "BEAVER":
            classes.append(Beaver())
        elif i == "CRICKET":
            classes.append(Cricket())
        elif i == "DUCK":
            classes.append(Duck())
        elif i == "FISH":
            classes.append(Fish())
        elif i == "HORSE":
            classes.append(Horse())
        elif i == "MOSQUITO":
            classes.append(Mosquito())
        elif i == "OTTER":
            classes.append(Otter())
        elif i == "PIG":
            classes.append(Pig())

    return classes


# 'f' stands for 'food'
def f_name_to_class(names):  # 'names' is list of string values of names of pet types
    classes = []  # same as 'names' but all string values are converted to the corresponding food class

    for i in names:  # matching each string value to its class
        if i == "APPLE":
            classes.append(Apple())
        elif i == "HONEY":
            classes.append(Honey())

    return classes
