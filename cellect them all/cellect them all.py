from random import choice
def cheak_coffee(list1,list2,):
  result =  all(elem in list1  for elem in list2)
  if result:
    print(f"Yes, your list of letters contains all the letters in coffee")
    return True
  else :
    print(f"no, your list of letters contains all the letters in coffee")
    return False
possible_letters = ["c","o","f","e"]
letters = []
CS = 100
OS = 150
FS = 300
ES = 350
for i in range (CS):
  letters.append("c")
for i in range (OS):
  letters.append("o")
for i in range (FS):
  letters.append("f")
for i in range (ES):
  letters.append("e")
print(letters)
my_letters = ['c','c','o','f','f','f','e','e']
free_coffee = ['c','o','f','f','e','e']
letter_to_add = choice(letters)
print (*my_letters, sep = ", ")
for i in range (4):
  value = possible_letters[i]
  enumerate(value)
  if my_letters.count(value) == 1:
    print(f"there are {my_letters.count(value)} {value} in your letters")
  else:
    print(f"there is {my_letters.count(value)} {value}'s in your letters")
if my_letters.count("f") >= 2 and my_letters.count("e") >= 2 and cheak_coffee(my_letters, free_coffee) == True:
  print("congradulations you've won a free coffee")

