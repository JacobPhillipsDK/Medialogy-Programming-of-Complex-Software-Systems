class champion:
    __name = "Default"
    __lane = "Default"

    def __init__(self, new_name="Default", new_lane="Default", new_level=1):
        self.__name = new_name
        self.__lane = new_lane
        self.__level = new_level

    def setName(self, new_name: str) -> None:
        self.__name = new_name

    def getName(self) -> str:
        return self.__name

    def setLane(self, new_lane: str) -> None:
        self.__lane = new_lane

    def getLane(self) -> str:
        return self.__lane

    def setLevel(self, new_level: int) -> None:
        self.__level = new_level

    def getLevel(self) -> int:
        return self.__level