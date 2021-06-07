
#The program creates and shuffles a deck of cards for a game of blackjack



import random

from Card import Card

card_values = [
 "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"
]

lands = [
 "S", "H", "D", "C"
]


class Deck:

    def __init__(self):

# create a deck of cards using the Card class
        self.__cards = [
            str(Card(l, value)) for value in card_values for l in lands
                         ]
        random.shuffle(self.__cards)

    def return_list(self):

        return self.__cards
