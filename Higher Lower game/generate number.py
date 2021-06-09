import random
goal = random.randint(1,100)
guess = 0
attempts = 0
guess_num = 10
while attempts < 10 :
  new_guess = int(input(f"please guess a number between 1 and 100 you have {guess_num} attempts left\n"))
  guess = new_guess
  attempts += 1
  guess_num -= 1
  if new_guess < goal :
    print ("guess a higher number")
  elif new_guess > goal :
    print ("guess a lower number")
  else:
    print (f"congradulations you guessed the number in {attempts} attempts")
    break
  if attempts == 10 :
    print (f"you used all your guesses up the number was {goal}")
    break