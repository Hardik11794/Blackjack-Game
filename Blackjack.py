from Modules import Hand
from Modules import Deck
from Modules import Cards


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
            break
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
    for card in Dealer.cards[2:]:
        print(card)
    print("Player's Hand")
    for card in Player.cards:
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
    
