############### Blackjack Project #####################

import random
import os

user_cards = []
computer_cards = []
continue_game=True

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card=random.choice(cards)
  return card

def calculate_score(cards):
  sum=0
  number=len(cards)
  for card in cards:
    sum+=card
  if number==2 and sum==21:
    return 0
  if 11 in cards and sum>21:
    cards.remove(11)
    cards.append(1)
  return sum

def compare(user,computer):
  if user==computer:
    return "Draw"
  elif computer==0:
    return "Lose, opponent has Blackjack"
  elif user==0:
    return "Win with a Blackjack"
  elif user > 21:
    return "You went over. You lose"
  elif computer > 21:
    return "Opponent went over. You win"
  elif user > computer:
    return "You win"
  else:
    return "You lose"
  
  
while continue_game:
  print(r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")
  user_cards = []
  computer_cards = []
  first=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if first=="y":
    # Clearing the Screen
    os.system('cls')
  else: 
    continue_game=False
    break
  for i in range (0,2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  print (f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
  print(f"Computer's first card: {computer_cards[0]}")
  user_score=calculate_score(user_cards)
  user_score=calculate_score(user_cards)
  computer_score=calculate_score(computer_cards)
  if user_score==0 or computer_score==0 or user_score>21:
    print ("Game over")
  else:
    option=input("Do you want to draw another card? Type 'y' or 'n': ")
    if option=="y":
      user_cards.append(deal_card())
      user_score=calculate_score(user_cards)
    else:
      continue_game=False
      print("Game over")
    if computer_score<17:
      computer_cards.append(deal_card())
      computer_score=calculate_score(computer_cards)
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print( compare(user_score,computer_score)   )
  restart=input("Do you want to restart the game? Type 'y' or 'n': ")
  if restart=="y":
    continue_game=True
    # Clearing the Screen
    os.system('cls')
  else:
    continue_game=False
