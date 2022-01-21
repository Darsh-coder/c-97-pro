
import random
number = random.randint(1, 10)
chances = 0

while (chances < 5):

    numberinput = int(input("Enter the number between 1-10: "))

    if (numberinput > number):
        print("Your guess is too large")
        
    elif (numberinput == number):
        print("Congratulation! YOU WON ")
        break

    else :
        print("Your number guess is too less")
    chances = chances + 1

if (chances > 5):
    print("YOU LOSE")
