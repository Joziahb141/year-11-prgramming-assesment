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
            value = True
        else:
            print ("PLEASE ENTER A WHOLE NUMBER BETWEEN 1 AND 10")
    except ValueError:
        print ("PLEASE ENTER A WHOLE NUMBER BETWEEN 1 AND 10")
print ("program finished")
