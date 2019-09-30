import random
from Modules import Cards   #Disable this line when you run __name__=='__main__':
#import Cards        #Enable this line when you run __name__=='__main__':

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
#*****************************************************************************************************
#      This class contains the cards, can shuffle it , can display the deck and open the single card
#*****************************************************************************************************
class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Cards.Cards(suit,rank))
    def __str__(self):
        deck_cards = ''
        for card in self.deck:
            deck_cards += '\n' + str(card)     
        return deck_cards
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card = self.deck.pop()
        return single_card


if __name__=='__main__':

    c = Deck()
    print(c)

    print(c.deal())
    print(c)

    c.shuffle()
    print(c)


    print(c.deal())








