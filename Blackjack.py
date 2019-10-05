from Modules import Hand
from Modules import Deck
from Modules import Cards
from Modules import Chips


playing = True


#*****************************************************************************************************
#      This function ask player for Hit or Stand
#*****************************************************************************************************


def hit_or_stand(Deck,Hand):

  global playing  # to control an upcoming while loop

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


#*****************************************************************************************************
#      This function shows card
#*****************************************************************************************************
    
def show_some(player,dealer):
    x=0
    print("\nDealer's Hand")
    print("\n<<<Card Hidden>>>")
    for card in dealer.cards[1:]:
        print(card)

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
   
 #*********************************************************************************************************
 #                   Game Arrangements
 #*********************************************************************************************************

while True:
    # Print an opening statement
    print("\n Welcome to BlackJack !!\n")

    
    # Create & shuffle the deck, deal two cards to each player
   
    
    Deck = Deck.Deck()
    Deck.shuffle()

    Players_Hand = Hand.Hand()
    Players_Hand.add_card(Deck.deal())
    Players_Hand.add_card(Deck.deal())

    Dealers_Hand = Hand.Hand()
    Dealers_Hand.add_card(Deck.deal())
    Dealers_Hand.add_card(Deck.deal())
        
    Player_Chips = Chips.Chips()

    # Prompt the Player for their bet
    take_bet(Player_Chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(Players_Hand,Dealers_Hand)
    
    

    
    while playing == True:  
      
        hit_or_stand(Deck,Players_Hand)
        show_some(Players_Hand,Dealers_Hand)
        print(playing)

        if Players_Hand.value > 21:
           player_busts(Players_Hand,Dealers_Hand,Player_Chips)
           break
           
        elif Players_Hand.value == 21:
            player_wins(Players_Hand,Dealers_Hand,Player_Chips)
            break
        
        elif playing == True and Players_Hand.value < 21:
           continue 
        else:
             while playing == False and Dealers_Hand.value <= 17:
                Dealers_Hand.add_card(Deck.deal())
                show_some(Players_Hand,Dealers_Hand)
             show_all(Players_Hand,Dealers_Hand)
           
             if Dealers_Hand.value > 21:
                dealer_busts(Players_Hand.value,Dealers_Hand,Player_Chips)
                break   
                  
             elif Players_Hand.value < Dealers_Hand.value:
                   player_busts(Players_Hand,Dealers_Hand,Player_Chips)
                   break

             elif Players_Hand.value > Dealers_Hand.value:
                   player_wins(Players_Hand,Dealers_Hand,Player_Chips)
                   break
             else:
                   push()
                   break
                

   
    
   
        
    
       
    

    print("\nPlayer's winnings stand at",Player_Chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
       playing=True
       continue
    else:
       print("Thanks for playing!")
    break
