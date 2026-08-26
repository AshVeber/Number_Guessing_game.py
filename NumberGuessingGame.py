import random

#greeting
class Greet:
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(f"Hello, {self.name}!\nWelcome to number guessing game!")

name = input("Type your name: ")
gree = Greet(name)
gree.greet()

#set low and high number
while True:
    try:
        low = int(input("Enter the lowest bound: "))
    except:
        print("Your input should be an integer.")
        continue
    else:
        break

while True:
    try:
        high = int(input("Enter the highest bound: "))
    except:
        print("Invalid input.")
        continue
    else:
        break

num = random.randint(low, high)

#total allowed chances
ch = 7
print(f"You have {ch} chances to win! Good luck <3")


#guess logic
class Guess:
    def __init__(self):
        self.__chance = 0
    def guess(self):
        while ch > self.__chance:
            while True:
                try:
                    gues_s = int(input("Your guess: "))
                except:
                    print("Type valid input.")
                    continue
                else:
                    break

            if num > gues_s:
                print("Too low!")
                self.__chance += 1
                continue
            elif num < gues_s:
                print("Too high!")
                self.__chance += 1
                continue
            else:
                print(f"You win! It's {num}")
                break
        print("You out of chances :(")

guess = Guess()
guess.guess()
