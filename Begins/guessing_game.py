import random

number = random.randint(0, 10)

while True:
    choice = int(input("please pick a number.\n"))
    if choice == number:
        print("you won")
        break
    else:
        print("try again")
        continue
