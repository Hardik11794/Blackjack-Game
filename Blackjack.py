import random
from Modules import Cards
from Modules import Deck

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

c = Cards.Cards(suits[1],ranks[4])
print(c)

Deck.Deck(suits,ranks)

Deck.Deck.shuffle

d = Deck.Deck(suits,ranks)
print(d)
