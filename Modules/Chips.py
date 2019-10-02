
#*****************************************************************************************************
#      This class keeps record of avaialable bet, Total bet and win and loose functions
#*****************************************************************************************************

class Chips:
    
    def __init__(self):
        self.total = 100                # This can be set to a default value 
        self.bet = 0
        
    def win_bet(self):
        self.total += (self.bet*2)
        
    def lose_bet(self):
        self.total -= self.bet
        
#*****************************************************************************************************
#      This function ask for bet to the player
#*****************************************************************************************************

def take_bet(Chips):

    while True:
            try:
                Chips.bet = int(input("Please, Enter your bet : "))
            except:
                print("Enter interger numbers only.")
            else:
                if Chips.bet > Chips.total:
                    Print(f"Bet must be Less then availble balance {Chips.total}. ")
                    continue
                else:
                    break
            