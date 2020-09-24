import random
from Champions import champion

TopChamp = champion()
JglChamp = champion()
MidChamp = champion()
AdcChamp = champion()
SupChamp = champion()


def champ1(top):
    switcher = {
        0: "Garen",
        1: "Darius",
    }
    return switcher.get(top, "Invalid Champion")


def champ2(jgl):
    switcher = {
        0: "Fiddlesticks",
        1: "Warwick",
    }
    return switcher.get(jgl, "Invalid Champion")


def champ3(mid):
    switcher = {
        0: "Ahri",
        1: "Lux",
    }
    return switcher.get(mid, "Invalid Champion")


def champ4(adc):
    switcher = {
        0: "Vayne",
        1: "Draven",
    }
    return switcher.get(adc, "Invalid Champion")


def champ5(sup):
    switcher = {
        0: "Soraka",
        1: "Alistar",
    }
    return switcher.get(sup, "Invalid Champion")


TopChamp.setName(champ1(random.randint(0, 1)))
JglChamp.setName(champ2(random.randint(0, 1)))
MidChamp.setName(champ3(random.randint(0, 1)))
AdcChamp.setName(champ4(random.randint(0, 1)))
SupChamp.setName(champ5(random.randint(0, 1)))


print(TopChamp.getName(), "In toplane")
print(JglChamp.getName(), "In Jungle")
print(MidChamp.getName(), "In Midlane")
print(AdcChamp.getName(), "In Botlane as ADC")
print(SupChamp.getName(), "In Botlane as Support")
