from random import choice
play = True
options = ['ROCK','PAPER','SCISSORS']
bot_score = 0
user_score = 0
print("""
**************************************************
               Rock,Paper,Scissor
**************************************************
Welcome to the classic game of Rock,Paper,Scissors  
""")
valid = False
while not valid:
  try:
    games = int(input("How many rounds do you want to play?\n"))
    if 0 < games:
      valid = True
    else:
      print("PLEASA TYPE IN A WHOLE NUMBER")
  except ValueError:
    print("PLEASA TYPE IN A WHOLE NUMBER")
while games > 0 and play == True:
  games -= 1
  valid = False
  while not valid:
    try:
      user_choice = input("What would you like to choose Rock, Paper or Scissors?\n")
      if user_choice.upper() in options:
        valid = True
      else:
        print("PLEASA TYPE IN ROCK, PAPER OR SCISSORS")
    except ValueError:
      print("PLEASA TYPE IN ROCK, PAPER OR SCISSORS")
  bot_option = choice(options)

  if user_choice.upper() == options[0]:
    if bot_option == options[1]:
      print(f"the bot chose {bot_option.title()} you did {user_choice.title()} you lost!!")
      bot_score += 1
    elif bot_option == options[2]:
      print(f"the bot chose {bot_option.title()} you did {user_choice.title()} you won!!")
      user_score += 1
    else:
      print(f"the bot chose {bot_option.title()} you did {user_choice.title()} its a draw")
  elif user_choice.upper() == options[1]:
    if bot_option == options[2]:
      print(f"the bot chose {bot_option.title()} you did {user_choice.title()} you lost")
      bot_score += 1
    elif bot_option == options[0]:
      print(f"the bot chose {bot_option.title()} you did {user_choice.title()} you won!!")
      user_score += 1
    else:
      print(f"the bot chose {bot_option.title()} you did {user_choice.title()} its a draw")
  else:
    if bot_option == options[0]:
      print(f"the bot chose {bot_option.title()} you did {user_choice.title()} you lost")
      bot_score += 1
    elif bot_option == options[1]:
      print(f"the bot chose {bot_option.title()} you did {user_choice.title()} you won!!")
      user_score += 1
    else:
      print(f"the bot chose {bot_option.title()} you did {user_choice.title()} its a draw")
  print(f"your score is {user_score}\nthe computers score is {bot_score}")
print("****** Thankyou for playing ******")