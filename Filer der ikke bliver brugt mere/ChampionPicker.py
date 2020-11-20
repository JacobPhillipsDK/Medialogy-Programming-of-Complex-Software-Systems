import random
from Champions import champion
from colorama import Fore, Style

__TopChamp = champion()
__JglChamp = champion()
__MidChamp = champion()
__AdcChamp = champion()
__SupChamp = champion()

__TopChamp2 = champion()
__JglChamp2 = champion()
__MidChamp2 = champion()
__AdcChamp2 = champion()
__SupChamp2 = champion()

def __champ1(top):
    switcher = {
        0: "Garen",
        1: "Darius",
    }
    return switcher.get(top, "Invalid Champion")


def __champ2(jgl):
    switcher = {
        0: "Fiddlesticks",
        1: "Warwick",
    }
    return switcher.get(jgl, "Invalid Champion")


def __champ3(mid):
    switcher = {
        0: "Ahri",
        1: "Lux",
    }
    return switcher.get(mid, "Invalid Champion")


def __champ4(adc):
    switcher = {
        0: "Vayne",
        1: "Draven",
    }
    return switcher.get(adc, "Invalid Champion")


def __champ5(sup):
    switcher = {
        0: "Soraka",
        1: "Alistar",
    }
    return switcher.get(sup, "Invalid Champion")

def setblueteam() -> None:
    __TopChamp.setName(__champ1(random.randint(0, 1)))
    __JglChamp.setName(__champ2(random.randint(0, 1)))
    __MidChamp.setName(__champ3(random.randint(0, 1)))
    __AdcChamp.setName(__champ4(random.randint(0, 1)))
    __SupChamp.setName(__champ5(random.randint(0, 1)))
    print(Fore.BLUE + "Top -", __TopChamp.getName())
    print("Jungle -", __JglChamp.getName())
    print("Mid -", __MidChamp.getName())
    print("ADC -", __AdcChamp.getName())
    print("Support -", __SupChamp.getName())
    print(Style.RESET_ALL, "vs")

def setredteam() -> None:
    __TopChamp2.setName(__champ1(random.randint(0, 1)))
    __JglChamp2.setName(__champ2(random.randint(0, 1)))
    __MidChamp2.setName(__champ3(random.randint(0, 1)))
    __AdcChamp2.setName(__champ4(random.randint(0, 1)))
    __SupChamp2.setName(__champ5(random.randint(0, 1)))
    print(Fore.RED + "Top -", __TopChamp2.getName())
    print("Jungle -", __JglChamp2.getName())
    print("Mid -", __MidChamp2.getName())
    print("ADC -", __AdcChamp2.getName())
    print("Support -", __SupChamp2.getName())


def SetTeam(setblueteam, setredteam ):
    setblueteam()
    setredteam()

