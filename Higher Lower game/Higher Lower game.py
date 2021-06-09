from random import choice
play = True
numbers = []
maximum = 100
while play == True:
  for i in range(1,maximum):
    numbers.append(i)
  goal = choice(numbers)
  guesses = []
  attempts = 0
  guess_num = 10
  while attempts < 10:
    game_over = False
    guess = int(input(f"please guess a number between 1 and {maximum} you have {guess_num} attempts left\n"))
    valid = False
    while not valid:
        try:
            guess = int(input(f"please guess a number between 1 and {maximum} you have {guess_num} attempts left\n"))
            if 0 < guess <= maximum:
                valid = True
            else:
                print ("PLEASE ENTER A WHOLE NUMBER BETWEEN 1 AND 10")
        except ValueError:
            print ("PLEASE ENTER A WHOLE NUMBER BETWEEN 1 AND 10")
    if guess in guesses:
        print("You have already guessed this number please guess again")
    else:
        guesses.append(guess)
        attempts += 1
        guess_num -= 1
        if guess in nember:
            numbers.pop(guess)
    
        if guess < goal :
            print ("guess a higher number")
        elif guess > goal :
            print ("guess a lower number")
        else:
            print (f"congradulations you guessed the number in {attempts} attempts")
            game_over = True
        if attempts == 10:
            print (f"you used all your guesses up the number was {goal}")
            game_over = True
    if game_over == True:
        play_again = input("do you want to play again? if so press y ")
        if play_again != "y" or play_again != "Y":
            play = False
    
        
print("Thankyou for playing")