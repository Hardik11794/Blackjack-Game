from Modules import Hand
from Modules import Deck
from Modules import Cards
from Modules import Chips


playing = True
############################For Deck######################
#c = Deck.Deck()
#print(c)
#print(c.deal())
#print(c)
#c.shuffle()
#print(c)
#print(c.deal())
##########################################################

############################For Hand########################
#test_deck = Deck.Deck()
#test_deck.shuffle()
#test_player = Hand.Hand()
#test_player.add_card(test_deck.deal())
#test_player.add_card(test_deck.deal())
#print(test_deck.deal())
#print(test_player.value)
#for card in test_player.cards:
#    print(card)
#########################################################

#*****************************************************************************************************
#      This function ask player for Hit or Stand
#*****************************************************************************************************


def hit_or_stand(Deck,Hand):

    global playing  # to control an upcoming while loop

    while True:
       try:
        Choose_HitStand = str(input("Enter Hit or Stand, 'h' or 's' : " ))
       except:
        print("Only lower case string allowed.")
       else:    
        if Choose_HitStand[0].lower() == 'h':
            hit(deck,Hand)
           
        elif Choose_HitStand[0].lower() == 's':
            print('Player Stand,Dealer is Playing.')
            playing = False
            break
        else:
            print("Only write 'h' or 's' for Hit and Stand")
            continue


#*****************************************************************************************************
#      This function shows card
#*****************************************************************************************************
    

def show_some(player,dealer):
    print("Dealer's Hand")
    print("<<<Card Hidden>>>")
    for card in dealer.cards[2:]:
        print(card)
    print("Player's Hand")
    for card in player.cards:
        print(card)
 
    
def show_all(player,dealer):
    
    print("Dealer's Hand")
    for card in dealer.cards:
        print(card)
    print(dealer.value)

    print("Player's Hand")
    for card in player.cards:
        print(card)
    print(player.value)


#*******************************************************************************************************
#      This function takes hits
#******************************************************************************************************* 

def hit(deck,hand):
    add_card(deck.deal())
    hand.adjust_for_aces    


#*****************************************************************************************************
#      This function print player or dealer won or lose 
#*****************************************************************************************************

def player_busts(player,dealer,Chips):
    print("Player Busts!!!")
    chips.lose_bet()

def player_wins(player,dealer,Chips):
    print("Player Won!!!")
    chips.win_bet()

def dealer_busts(player,dealer,Chips):
    print("Dealer Busts!!!")
    chips.lose_bet()

def dealer_wins(player,dealer,Chips):
    print("Delaer Busts!!!")
    chips.win_bet()

def push():
    print("Dealer and Player tie! It's a push.")


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
                    print(f"Bet must be Less then availble balance {Chips.total}. ")
                    continue
                else:
                    break
   
 #*********************************************************************************************************
 #                   Game Arrangements
 #*********************************************************************************************************

while True:
    # Print an opening statement
    print("Welcome to BlackJack !!")

    
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
    
    

    
    while playing == True:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
                 hit_or_stand(Deck.Deck,Players_Hand)
        
        # Show cards (but keep one dealer card hidden)
                 show_some(Players_Hand,Dealers_Hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
                 if Players_Hand.value > 21:
                   player_busts(Players_Hand,Dealers_Hand,Chips)

                   break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
                 else:
                     while Dealers_Hand.value <= 17:
                            Dealers_Hand.add_card(Deck.deal())
    
        # Show all cards
                 show_all(Players_Hand,Dealers_Hand)
        # Run different winning scenarios
                 if Players_Hand.value < Delears_Hand.value:
                      player_busts(Players_Hand,Dealers_Hand,Chips)
                 elif Players_Hand.value > Dealers_Hand.value:
                     player_wins(Players_Hand,Dealers_Hand,Chips)
                 elif Delears_Hand.value > 21:
                      dealer_wins(Players_Hand.value,Dealers_Hand,Chips)
                 else:
                      push(player_hand,dealer_hand)

    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break
    # Inform Player of their chips total 
    
    # Ask to play again

        break