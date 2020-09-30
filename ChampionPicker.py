import random
from Champions import champion
from colorama import Fore, Back, Style

TopChamp = champion()
JglChamp = champion()
MidChamp = champion()
AdcChamp = champion()
SupChamp = champion()

TopChamp2 = champion()
JglChamp2 = champion()
MidChamp2 = champion()
AdcChamp2 = champion()
SupChamp2 = champion()

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

def setblueteam() -> None:
    TopChamp.setName(champ1(random.randint(0, 1)))
    JglChamp.setName(champ2(random.randint(0, 1)))
    MidChamp.setName(champ3(random.randint(0, 1)))
    AdcChamp.setName(champ4(random.randint(0, 1)))
    SupChamp.setName(champ5(random.randint(0, 1)))
    print(Fore.BLUE + "Top -", TopChamp.getName())
    print("Jungle -", JglChamp.getName())
    print("Mid -", MidChamp.getName())
    print("ADC -", AdcChamp.getName())
    print("Support -", SupChamp.getName())
    print(Style.RESET_ALL, "vs")

def setredteam() -> None:
    TopChamp2.setName(champ1(random.randint(0, 1)))
    JglChamp2.setName(champ2(random.randint(0, 1)))
    MidChamp2.setName(champ3(random.randint(0, 1)))
    AdcChamp2.setName(champ4(random.randint(0, 1)))
    SupChamp2.setName(champ5(random.randint(0, 1)))
    print(Fore.RED + "Top -", TopChamp2.getName())
    print("Jungle -", JglChamp2.getName())
    print("Mid -", MidChamp2.getName())
    print("ADC -", AdcChamp2.getName())
    print("Support -", SupChamp2.getName())


def SetTeam(setblueteam, setredteam ):
    setblueteam()
    setredteam()

