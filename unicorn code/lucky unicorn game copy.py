from random import choice

print ("""
**********Lucky Unicorn**********
Welcome to the Lucky yunicorn game wher you can try your luck 
But dont get a donkey!
*********************************
""")


valid = False
while not valid:
    try:
        Dollars = int(input("if you wish to play please pay $1 per round with a max of $10.\nHow much do you want to pay? "))
        if 0 < Dollars <= 10:
            valid = True
        else:
            print ("PLEASE ENTER A WHOLE NUMBER BETWEEN 1 AND 10")
    except ValueError:
        print ("PLEASE ENTER A WHOLE NUMBER BETWEEN 1 AND 10")
Keep_Going = True
won = 0.0
horse_num = 550
zebra_num = 500
donkey_num = 45
unicorn_num = 5
tokens = []
for i in range(horse_num):
    tokens.append('horse')

for i in range(zebra_num):
    tokens.append('zebra')

for i in range(donkey_num):
    tokens.append('donkey')

for i in range(unicorn_num):
    tokens.append('unicorn')

while Keep_Going == True and Dollars >0:
    token = choice(tokens)
    Dollars -= 1
    print(token)
    rewards = {'horse': 0.5,
                'zebra': 0.5,
                'donkey': 0,
                'unicorn': 5}
    reward = rewards[token]
    won += reward
    if token != 'donkey' or token != 'unicorn':
        print (f"Your Tocken was a {token} you won ${reward}")
        print (f"Your current ernings are {won}, you have ${Dollars} left")
    elif token == 'donkey':
        print (f"Oh no your Tocken was a {token} you won nothing")
        print (f"Your current ernings are {won}, you have ${Dollars} left")
    else:
        print (f"congradulations you got a {token} tocken. you won ${reward}!!!")
        print (f"Your current ernings are {won}, you have ${Dollars} left")
    play_again = input("do you wish to continue playing ? if so press y then enter ")
    if play_again == "y" or play_again == "Y":
        continue
    else:
        cheak = input("Are you sure you don't want to play again? if so press y ")
    if cheak == 'y' or cheak == 'Y':
        Keep_Going = False


print("Thankyou for playing the lucky unicorn game")

    

    
