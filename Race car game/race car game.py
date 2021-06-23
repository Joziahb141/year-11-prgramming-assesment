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
def roll_two_dice():
    return roll_dice() + roll_dice()
cars = []
for i in range (12):
    cars.append(0)
car_choice = get_int_input(f"choose a car between 1 and {len(cars)} ?\n","Please enter a number from 1 to 6",1,len(cars))
race_distance = get_int_input("choose a race distance between 5 and 15 ?\n","Please enter a number from 5 to 15",5,15)
print(roll_dice)
os.system('cls')
while len([i for i in cars if i >= 15]) < 3:
    for i, car in enumerate(cars):
        if i >= race_distance:
            print("-" * car + "o=o" + "\033[1;32;40m")
        elif i == car_choice - 1:
            print("-" * car + "o=o" + "\033[1;31;40m")
        else:
            print("-" * car + "o=o" + "\033[1;33;40m")
    input("push enter to continue")
    os.system('cls')
    cars[roll_two_dice()-1] += 1
    if cars[roll] < 15:
        cars[roll] += 1

sorted_cars = sorted(cars)
winning_car = cars.index(max(cars)) + 1

print (f"car {winning_car} won!!!")
if winning_car ==  car_choice:
    print("your car won!")
else:
    print("you didn't win")

for i, in car in enumerate(positions):
    print(f"Car number {car} came in position {i + 1}")

