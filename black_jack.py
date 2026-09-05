############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.


import random
#from art import logo

user_cards=[]
computer_cards=[]


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    ret=0
    aces=0
    for card in cards:
        ret+=card
        if card==11: aces=aces+1
    while aces>0 and ret>21:
        ret-=10
        aces=aces-1
    return ret


    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    # Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw.
    # If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses.
    # If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.


def compare(user_score, computer_score):
    if user_score>computer_score or computer_score>21: return 1
    if user_score==computer_score: return 0
    return -1


def showusercards():
    print("Your cards:", user_cards)

def showcomputercards():
    print("Dealer cards:", computer_cards)


def play_game():
    user_cards.clear()
    computer_cards.clear()
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())
    if calculate_score(user_cards)==21:
        if calculate_score(computer_cards)==21: 
            print("Draw")
        else:
            print("You lost")
        return
    user_score=0
    showusercards()
    while input("Do you want another card? Type 'y' or anything else for no: ") == "y":
        user_cards.append(deal_card())
        showusercards()
        user_score=calculate_score(user_cards)
        if user_score>=21: break
    if user_score>21:
        print("You lost")
        return 
    computer_score=calculate_score(computer_cards)
    if user_score==21 and computer_score<21:
        print("You won")
        return
    while computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
    showcomputercards()
    winner=compare(user_score, computer_score)
    if winner==1: print("You won")
    elif winner==-1: print("You lost")
    else: print("Draw")
    


    



    # Hint 5: Deal the user and computer 2 cards each using deal_card()
    # Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    # Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List.
    # If no, then the game has ended.
    # Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    # Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.


# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
