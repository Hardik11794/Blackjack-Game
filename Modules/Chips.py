
#*****************************************************************************************************
#      This class keeps record of avaialable bet, Total bet and win and loose functions
#*****************************************************************************************************

class Chips:
    
    def __init__(self):
        self.total = 100                # This can be set to a default value 
        self.bet = 0
        
    def win_bet(self):
        self.total += (self.bet*2)
        
    def loose_bet(self):
        self.total -= self.bet
        
`