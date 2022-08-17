# message ="hello \n\"may\""
first = "may"
last = "cham"
full = first + " " + last
print(len(full))
# program to print number 8 using operators
print(5 + 3)
print(10 - 2)
print(80 / 10)
print(4 * 2)

# concatenating a string with an integer
x = 14
message = "my favorite number is"
print(message + " " + str(x))

# list in python
names = ["may", "sally", "bintou", "fatoumatta"]
speech = f"my first name is {names[0].title()}"
print(speech)
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(f"good morning {names[0].title()}")
print(f"good morning {names[1].title()}")
print(f"good morning {names[2].title()}")
print(f"good morning {names[3].title()}")

# list

guest_list = ["minny", "manny", "moo"]
print(f"\n hey {guest_list[0]} you are invited to the dinner")
print(f"\n hey {guest_list[1]} you are invited to the dinner")
print(f"\n hey {guest_list[2]} you are invited to the dinner")
print("\n")
guest_removed = guest_list.pop(0)

print(f"{guest_removed.title()} is not attending the dinner")

guest_list.insert(0, "mickey")

print("hey i have found a bigger dinner table")

guest_list.insert(0, "betty")
guest_list.insert(1, "matty")
guest_list.insert(2, "fatty")
guest_list.append("batty")

print(f"\n hey {guest_list[0]} you are invited to the dinner")
print(f"\n hey {guest_list[1]} you are invited to the dinner")
print(f"\n hey {guest_list[2]} you are invited to the dinner")
print(f"\n hey {guest_list[3]} you are invited to the dinner")
print(f"\n hey {guest_list[4]} you are invited to the dinner")
print(f"\n hey {guest_list[5]} you are invited to the dinner")
print(f"\n hey {guest_list[6]} you are invited to the dinner")

guest_removed0 = guest_list.pop(0)
print(f"\n hey {guest_removed0} you are not invited to the dinner")
guest_removed1 = guest_list.pop(1)
print(f"\n hey {guest_removed1} you are not invited to the dinner")
guest_removed2 = guest_list.pop(2)
print(f"\n hey {guest_removed2} you are not invited to the dinner")
guest_removed3 = guest_list.pop(3)
print(f"\n hey {guest_removed3} you are not invited to the dinner")
print("hey guys am sorry to tell you all that i can only invite two people\n")

for guest in guest_list:
    print(guest)

for number in range(4):
    print("hello world!")