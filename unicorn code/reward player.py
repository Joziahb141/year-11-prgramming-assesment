from random import choice
tockens = ['Zebra','Zebra','Zebra','Zebra','Horse','Horse','Horse','Horse','Donkey','Donkey','Unicorn']
response = choice(tockens)
print (f"Your tocken is a {response}")
if response == 'Horse' or response == 'Zebra':
    print("you won 50c")
elif response == 'Donkey':
    print("sorry you didn't win anything")
else:
    print("Congratulations you won $5 !!!")

