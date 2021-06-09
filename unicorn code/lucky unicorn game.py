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
tockens = ['Zebra','Zebra','Zebra','Zebra','Zebra','Zebra','Zebra','Zebra','Horse','Horse','Horse','Horse','Horse','Horse','Horse','Horse','Horse','Horse','Donkey','Donkey','Donkey','Donkey','Unicorn']

while Dollars != 0 and Keep_Going == True:
    response = choice(tockens)
    print (f"\nYour tocken is a {response}")
    if response == 'Horse' or response == 'Zebra':
        print("you won 50c")
        won += 0.5
    elif response == 'Donkey':
        print("sorry you didn't win anything")
    else:
        print("Congratulations you won $5 !!!")
        won += 5.0
    Dollars -= 1
    print(f"You have ${Dollars}")
    keep_goind = input("do you wish to continue playing ? if so press y")
    if keep_going != "y" or keep_going != "Y":
        Keep_Going = False
print("**********thankyou for playing**********")
