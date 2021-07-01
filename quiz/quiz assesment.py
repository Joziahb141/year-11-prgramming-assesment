import requests
from quiz_class import user1
print(user1)

questions = response.json()['results']
reponse = requests.get("https://opentdb.com/api.php?amount=10&category=29&type=multiple")
def get_integer_input(message, error, low, high):
    while True:
        try:
            inpt = int(input(message))
            if low < inpt < high or low == inpt or high == inpt:
                return inpt
            else:
                print(error)
        except ValueError:
            print(error)

user_choice = get_int_input 
def cheak_anwser():
  for i ,question in enumerate(questions):
    print("")