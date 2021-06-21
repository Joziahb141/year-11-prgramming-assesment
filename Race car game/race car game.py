import random
import os
def get_int_input(message, error, low, high):
    while True:
        try:
            inpt = int(input(message))
            if low < inpt < high or low == inpt or high == inpt:
                return inpt
            else:
                print("error")
        except ValueError:
            print(error)
def roll_dice():
    return random.randint(1, 6)

car_choice = get_int_input("choose a car between 1 and 6 ?\n","Please enter a number from 1 to 6",1,6)
race_distance = get_int_input("choose a race distance between 5 and 15 ?\n","Please enter a number from 5 to 15",5,15)
print(roll_dice)
cars = [0,0,0,0,0,0]
os.system('cls')
while max(cars) < race_distance:
    for i, car in enumerate(cars):
        print("-" * car + "o=o")
    input("push enter to continue")
    os.system('cls')
    cars[roll_dice()-1] += 1

winning_car = cars.index(max(cars)) + 1
print (f"car {winning_car} won!!!")