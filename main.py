from art import logo, vs
from random import choice
from game_data import data
from replit import clear

def compare_followers(a, b):
  if a > b:
    return "a"
  else:
    return "b"

def get_highest_followers(a, b):
  if a['follower_count'] > b['follower_count']:
    return a
  else:
    return b

def format_text(a):
  return f"{a['name']}, a {a['description'].lower()}, from {a['country']}."

def game(a, b , score):
  print(f"Compare A: {format_text(a)} ")
  # print(f"Psst... follower count: {a['follower_count']} ") # for debugging
  print(vs)
  print(f"Against B: {format_text(b)} ")
  # print(f"Psst... follower count: {b['follower_count']} ") # for debugging
  user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  answer = compare_followers(a['follower_count'], b['follower_count'])
  winning_option = get_highest_followers(a, b)
  b = choice(data) # get the next option B
  while winning_option == b: # in case the RNG picks winning option from the last round
    b = choice(data) # get it to pick a new option
  if user_guess == answer:
    score += 1
    clear()
    print(logo)
    print(f"Yay! You're right. Current score: {score}")
    game(winning_option, b, score)
  else:
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    restart = input("Type 'Y' to play again, 'N' to quit. ").lower()
    if restart == "y":
      score = 0
      clear()
      print(logo)
      game(winning_option, b, score)
    else:
      return

score = 0
start_a = choice(data)
start_b = choice(data)

while start_a == start_b:
    start_b = choice(data)

print(logo)    
game(start_a, start_b, score)
