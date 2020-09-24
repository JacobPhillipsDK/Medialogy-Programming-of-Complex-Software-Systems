import Player
from random import *

top = int
jgl = int
mid = int
adc = int
sup = int

def get_top_champion(top):
    switcher = {
    0: "Garen",
    1: "Darius",
}

def get_jgl_champion(jgl):
    switcher = {
    0: "Fiddlesticks",
    1: "Warwick",
}

def get_mid_champion(mid):
    switcher = {
    0: "Ahri",
    1: "Lux",
}

def get_adc_champion(adc):
    switcher = {
    0: "Vayne",
    1: "Draven",
}

def get_sup_champion(sup):
    switcher = {
    0: "Soraka",
    1: "Alistar",
}

if  Player.__lane == "top":
    print (get_top_champion(random(0-1)))
