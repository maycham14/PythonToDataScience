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

# may = [val ** 3 for val in range(1, 10)]
# print(may)

# while True:
#     message = int(input("please enter the age.\n"))
#     print()
#     if message < 3:
#         print("the ticket fee is $10 ")
#     elif 3 >= message >= 12:
#         print("your ticket is $15")
#     elif message > 12:
#         print("your ticket is $20")
#     else:
#         break
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)

sandwich_orders = ["plain", "filled", "extra", "plenty"]
finished_sandwich = []
while sandwich_orders:
    for sandwich in sandwich_orders:
        print(f"i made your {sandwich} sandwich.")
    finished_sandwich_orders = sandwich_orders.pop()
    finished_sandwich.append(finished_sandwich_orders)
    for sandwich in finished_sandwich:
        print(f"{sandwich} was made.\n")

responses = {}
active = True
while active:
    name = input("where would you love to visit?.\n")
    responses[name] = name
    if name.lower() == "quit":
        break
print(responses.keys())
