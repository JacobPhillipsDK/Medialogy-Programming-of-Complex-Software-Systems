class Player:
    __name = "Default"


    def __init__(self, new_name="Default"):
        self.__name = new_name

    def setName(self, new_name: str) -> None:
        self.__name = new_name

    def getName(self) -> str:
        return self.__name



