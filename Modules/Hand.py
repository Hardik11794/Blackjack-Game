from Modules import Deck   #Disable this line when you run __name__=='__main__':
#import Deck               #Enable this line when you run __name__=='__main__':


values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1


    def adjust_for_aces(self):
        if self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1



#*******************************************************************************************************
#      Troubleshoot class locally
#*******************************************************************************************************        
if __name__=='__main__':

    test_deck = Deck()
    test_deck.shuffle()
    test_player = Hand()

    test_player.add_card(test_deck.deal())

    test_player.add_card(test_deck.deal())

    print(test_player.value)

    for card in test_player.cards:
        print(card)



