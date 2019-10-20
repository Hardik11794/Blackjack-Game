from Modules import Hand
from Modules import Deck
from Modules import Cards
from Modules import Chips
from Modules import ServiceFunctions



#global playing  
playing = True

 #*********************************************************************************************************
 #                                    Game Arrangements
 #*********************************************************************************************************
Player_Chips = Chips.Chips()
while True:
    # Print an opening statement
    print("\n Welcome to BlackJack !!\n")

    
    # Create & shuffle the deck, deal two cards to each player
   
 
    Deck_cards = Deck.Deck()
    Deck_cards.shuffle()

    Players_Hand = Hand.Hand()
    Players_Hand.add_card(Deck_cards.deal())
    Players_Hand.add_card(Deck_cards.deal())

    Dealers_Hand = Hand.Hand()
    Dealers_Hand.add_card(Deck_cards.deal())
    Dealers_Hand.add_card(Deck_cards.deal())
        
   
    # Prompt the Player for their bet
    ServiceFunctions.take_bet(Player_Chips)
    
    # Show cards (but keep one dealer card hidden)
    ServiceFunctions.show_some(Players_Hand,Dealers_Hand)

    if Players_Hand.value == 21:
        ServiceFunctions.player_wins(Players_Hand,Dealers_Hand,Player_Chips)
        playing = False;
    
    while playing == True:  
      
        playing = ServiceFunctions.hit_or_stand(Deck_cards,Players_Hand,playing)
        ServiceFunctions.show_some(Players_Hand,Dealers_Hand)
        print(playing)

        if Players_Hand.value > 21:
           ServiceFunctions.player_busts(Players_Hand,Dealers_Hand,Player_Chips)
           break
           
        elif Players_Hand.value == 21:
            ServiceFunctions.player_wins(Players_Hand,Dealers_Hand,Player_Chips)
            break
        
        elif playing == True and Players_Hand.value < 21:
           continue 
        else:
             while playing == False and Dealers_Hand.value <= 17:
                Dealers_Hand.add_card(Deck_cards.deal())
                ServiceFunctions.show_some(Players_Hand,Dealers_Hand)
             ServiceFunctions.show_all(Players_Hand,Dealers_Hand)
           
             if Dealers_Hand.value > 21:
                ServiceFunctions.dealer_busts(Players_Hand.value,Dealers_Hand,Player_Chips)
                break   
                  
             elif Players_Hand.value < Dealers_Hand.value:
                   ServiceFunctions.player_busts(Players_Hand,Dealers_Hand,Player_Chips)
                   break

             elif Players_Hand.value > Dealers_Hand.value:
                   ServiceFunctions.player_wins(Players_Hand,Dealers_Hand,Player_Chips)
                   break
             else:
                   ServiceFunctions.push()
                   break    

    print("\nPlayer's winnings stand at",Player_Chips.total)
    
    # Ask to play again
    new_game = input("\nWould you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
       playing=True
       continue
    else:
       print("Thanks for playing!")
    break
