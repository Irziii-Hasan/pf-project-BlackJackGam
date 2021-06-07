#Category to clarify card handling



class Card:

    def __init__(self, l, value):

        self.__l = l
        self.__value = value

    def __str__(self):

        return self.__value + self.__l

    def l(self):

        return self.__l

    def value(self):

        return self.__value
