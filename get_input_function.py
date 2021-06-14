def get_int_input(message, error, low, high):
    while True:
        try:
            inpt = int(input(message))
            if low < inpt < high:
                return inpt
        except ValueError:
            print(error)
        
guesses = get_int_input("How many turns do you want\n","Please enter a number above zero or below 100",0,100)
print (f"you want to play {guessses} games")