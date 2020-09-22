class Player:
    __name = "Default"
    __lane = "Default"
    __age = 0

    def __init__(self, new_name="Default", new_lane="Default", new_age=0):
        self.__name = new_name
        self.__lane = new_lane
        self.__age = new_age

    def setName(self, new_name: str) -> None:
        self.__name = new_name

    def getName(self) -> str:
        return self.__name

    def setLane(self, new_lane: str) -> None:
        self.__lane = new_lane

    def getLane(self) -> str:
        return self.__lane
