class Deck:

    def __init__(self,suits,ranks):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append( rank + ' of ' + suit)
        #print(self.deck)
    def __str__(self):
       return self.deck[0]
    
    def shuffle(self):
        random.shuffle(self.deck)




