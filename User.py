class User:
    def __innit__(self,name: str, age: str, money: int):
        self.__name = name
        self.__age = age
        self.__money = money

    def get_Name(self):
        return self.__name

    def get_Money(self):
        return self.__money

    def set_money(self,newmoney: int):
        self.__money = newmoney
