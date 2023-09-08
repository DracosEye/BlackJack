############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
from random import choice
from art import logo
from replit import clear

while True:
  #Decide whether or not to continue
  cont = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if cont != 'y':
    break
  else:
    clear()
    print(logo)
    
  #Initialize hands
  player_cards = []
  dealer_cards = []
  hit = True
  blackjack = False
  
  #Deal the cards
  for _ in range(2):
    player_cards.append(choice(cards))
    dealer_cards.append(choice(cards))

  #Blackjack
  if sum(player_cards) == 21 or sum(dealer_cards) == 21:
    blackjack = True
    break
  
  #Dealer hits until 17 or higher
  while sum(dealer_cards) < 17:
    new_card = choice(cards)
    if new_card == 11 and sum(dealer_cards) > 10:
      new_card = 1
    dealer_cards.append(new_card)
  dealer_score = sum(dealer_cards)

  #Play the hand until player doesn't want any more hits
  while True:
    
    player_score = sum(player_cards)
    if player_score > 21:
      #If player has an ace and goes over 21, change the 11 to a 1
      if 11 in player_cards:
        player_score -= 10
        player_cards[player_cards.index(11)] = 1
      else:
        break
    #Give summary of situation
    print(f"   Your cards: {player_cards}, current score: {player_score}")
    print(f"   Computer's first card: {dealer_cards[0]}")
  
    hit = input("Type 'y' to get another card, type 'n' to pass: ")
    if hit != 'y':
      break
    else:
      player_cards.append(choice(cards))

  #Give final hands and scores.
  print(f"   You final hand: {player_cards}, final score: {player_score}")
  print(f"   Computer's final hand: {dealer_cards}, final score: {dealer_score}")

  #Give final results
  if player_score > 21:
    print("You went over. You lose 😤")
  elif dealer_score > 21:
    print("Opponent went over. You win 😃")
  elif player_score == dealer_score:
    print("Draw")
  elif blackjack:
    if player_score == 21:
      print("Win with a Blackjack 😎")
    else:
      print("Lose, opponent has Blackjack 😱")
  elif dealer_score > player_score:
    print("You lose 😤")
  else:
    print("You win 😃")