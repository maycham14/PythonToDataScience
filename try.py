# age = 12
# if 0 <= age < 21:
#     print("am not legal")
# else:
#     print("am legal")
#
# message = "eligible" if age <= 23 else "not eligible"
# print(message)
#
# for x in range(4):
#     for y in range(4):
#         print(f"{x} and {y}")
# count = 0
# for number in range(1, 10):
#     if number % 2 == 0:
#         count = count + 1
#         print(number)
# print(f"we have {count} even numbers")
#
# square = []
# for value in range(1, 11):
#     squares = value ** 2
#     square.append(squares)
# print(square)
# print("\n")
#
# summ = sum(range(1, 1_0001))
# print(summ)
#
# for let in range(1, 21, 2):
#     print(let)
#
# multiples = [3, 9, 12, 15, 18, 21]
# for multiple in multiples:
#     print(multiple)
# cubes = []
# for value in range(1, 11):
#     cube = value ** 3
#     cubes.append(cube)
# print(cubes)
#
# lists = []
# for i in range(1, 11):
#     lists.insert((i - 1), i ** 3)
#
# print(lists)
#
# may = [val ** 3 for val in range(1, 10)]
# print(may)

person = {"name": "mariama", "last_name": "cham", "age": 22, "city": "paris"}
print(person["name"] + "\n" + person["last_name"] + "\n" + str(person["age"]) + "\n" + person["city"])

favorite_language = {"mariama": "c", "fatima": "python", "john": "javascript"}
friend = ["fatima", "may"]
for favorite in favorite_language.keys():
    if favorite in friend:
        print(f"\t{favorite}, you are in the pool")
    else:
        print(f"\n{favorite} take the pool")

# dictionaries

# person1 = {"username": "maycham14", "first_name": "may", "last_name": "cham", "location": "fajikunda"}
# person2 = {"username": "tijou06", "first_name": "sheikh", "last_name": "hydara", "location": "bijilo"}
# people = [person1, person2]
#
# for key, value in person1.items():
#     print(f"{key}: {value}")
# print("\n")
# for key, value in person2.items():
#     print(f"{key}: {value}")

# the input function
# rental_car = input("please enter the car you would like:\n")
# print(f"let me see if {rental_car} is available.")
#
# seating = int(input("how many people are in the dining group?."))
#
# if seating > 8:
#     print("you would have to wait for a table.")
# else:
#     print("table is ready.")

# while loops
topping = input("please enter the topping you want.\n")

while True:
    message = topping
    if message == "quit":
        break
    else:
        print(f"{topping} will be added to your pizza\n")

print("Hello")