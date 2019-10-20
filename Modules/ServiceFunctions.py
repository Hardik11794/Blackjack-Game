from Modules import Hand
#global playing  

#*****************************************************************************************************
#      This function ask player for Hit or Stand
#*****************************************************************************************************


def hit_or_stand(Deck,Hand,playing):
 # global playing
  
  while True:
    Choose_HitStand = str(input("\nEnter Hit or Stand, 'h' or 's' : " ))
      
    if Choose_HitStand[0].lower() == 'h':
        hit(Deck,Hand)
        break
    elif Choose_HitStand[0].lower() == 's':
        print('\nPlayer Stand,Dealer is Playing.')
        playing = False
        break
    else:
          print("Only write 'h' or 's' for Hit and Stand")
          continue  

  return playing

#*****************************************************************************************************
#      This function shows card
#*****************************************************************************************************
    
def show_some(player,dealer):
  
    print("\nDealer's Hand")
    print("\n<<<Card Hidden>>>")
    for card in dealer.cards[1:]:
        print(card)
    print(dealer.value - Hand.values[dealer.cards[0].rank])

    print("\nPlayer's Hand\n")
    for card in player.cards:
        print(card)
    print(player.value)
    
def show_all(player,dealer):
    
    print("\nDealer's Hand\n")
    for card in dealer.cards:
        print(card)
    print(dealer.value)

    print("\nPlayer's Hand\n")
    for card in player.cards:
        print(card)
    print(player.value)

#*******************************************************************************************************
#      This function takes hits
#******************************************************************************************************* 

def hit(deck,Hand):
    Hand.add_card(deck.deal())
    Hand.adjust_for_aces    

#*****************************************************************************************************
#      This function print player or dealer won or lose 
#*****************************************************************************************************

def player_busts(player,dealer,Chips):
    print("\nPlayer Busts!!!\n")
    Chips.lose_bet()

def player_wins(player,dealer,Chips):
    print("\nPlayer Won!!!\n")
    Chips.win_bet()

def dealer_busts(player,dealer,Chips):
    print("\nDealer Busts!!!\n")
    Chips.lose_bet()

def dealer_wins(player,dealer,Chips):
    print("\nDelaer Busts!!!\n")
    Chips.win_bet()

def push():
    print("\nDealer and Player tie! It's a push.\n")


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
                    print(f"Bet must be less then availble balance {Chips.total}. ")
                    continue
                else:
                    break