from random import choice
def get_int_input(message, error, low, high):
    while True:
        try:
            inpt = int(input(message))
            if low < inpt < high:
                return inpt
            else:
                print(error)
        except ValueError:
            print(error)
        
maximum = get_int_input("how high do you want the random number to possible be?\n","PLEASE ENTER A POSITIVE WHOLE NUMBER BETWEEN 1 AND 1000",1,1000)
minimum = get_int_input("whats the lowest number the random number could be?\n",F"PLEASE ENTER A POSITIVE WHOLE NUMBER LESS THAN THE MAXIMUM OF {maximum} AND MORE THAN 0",0,maximum)
numbers = []
for i in range (minimum,(maximum+1)):
    numbers.append(i)

attempts = 0
game_over = False
guess = -1
print(numbers)
while attempts < 10 :
    guesses = []
    print(guesses)
    game_over == False
    goal = choice(numbers)
    while guess != goal:
        guess = get_int_input(f"please guess a number between {minimum} and {maximum} you have {10 - attempts} attempts left\n",f"ERROR PLEASE ENTER A WHOLE NUMBER BETWEEN {maximum} AND {minimum}!!!",minimum + 1,maximum + 1)
        guesses.append(guess)
        numbers.remove(guess)
        attempts += 1
        if attempts == 10 :
            print (f"you used all your guesses up the number was {goal}")
            game_over == True
            numbers.extend(guesses)
            numbers.sort
            print(numbers)
            del guesses
        else:
            if guess < goal :
                print ("guess a higher number")
            elif guess > goal :
                print ("guess a lower number")
            else:
                print (f"congradulations you guessed the number in {attempts} attempts")
                game_over == True
                numbers.extend(guesses)
                numbers.sort
                print(numbers)
                print(guesses)
                del guesses
