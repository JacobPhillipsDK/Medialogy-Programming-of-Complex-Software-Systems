from numpy import random
from Champions import champion

top = int
jgl = int
mid = int
adc = int
sup = int

# Toplane champs
Garen = champion()
Garen.setName("Garen")
Garen.setLane("top")

Darius = champion()
Darius.setName("Darius")
Darius.setLane("top")

# Jungle Champs
Fiddlesticks = champion()
Fiddlesticks.setName("Fiddlesticks")
Fiddlesticks.setLane("jgl")

Warwick = champion()
Warwick.setName("Warwick")
Warwick.setLane("jgl")

# Mid Champs
Ahri = champion()
Ahri.setName("Ahri")
Ahri.setLane("mid")

Lux = champion()
Lux.setName("Lux")
Lux.setLane("mid")

# ADC Champs
Vayne = champion()
Vayne.setName("Vayne")
Vayne.setLane("adc")

Draven = champion()
Draven.setName("Draven")
Draven.setLane("adc")

# Support Champs
Soraka = champion()
Soraka.setName("Soraka")
Soraka.setLane("sup")

Alistar = champion()
Alistar.setName("Alistar")
Alistar.setLane("sup")


def get_top_champion(top):
    switcher = {
        0: Garen.getName(),
        1: Darius.getName(),
    }


def get_jgl_champion(jgl):
    switcher = {
        0: Fiddlesticks,
        1: Warwick,
    }


def get_mid_champion(mid):
    switcher = {
        0: Ahri,
        1: Lux,
    }
    return switcher.get(mid)


def get_adc_champion(adc):
    switcher = {
        0: Vayne,
        1: Draven,
    }


def get_sup_champion(sup):
    switcher = {
        0: Soraka,
        1: Alistar,
    }


# Brug if statement til at hente champs, og switch til at store champions.

print(get_mid_champion(0))
