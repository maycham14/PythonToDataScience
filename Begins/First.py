# guest = ["miny", "many", "moo"]
# print(f"\n hey {guest[0].title()} you are invited")
# print(f"\n hey {guest[1].title()} you are invited")
# print(f"\n hey {guest[2].title()} you are invited")
# print("\n")
# print(f"\n hey {guest[0].title()} cannot make it to the dinner")
#
# del guest[0]
# guest.insert(0, "fatou")
#
# print(f"\n hey {guest[0].title()} you are invited")
# print(f"\n hey {guest[1].title()} you are invited")
# print(f"\n hey {guest[2].title()} you are invited")
# print("\n")
# print("ive found a bigger dinner table")
#
# guest.insert(0, "binta")
# guest.insert(2, "sally")
# guest.append("bella")
#
# print("\n")
# # print("sorry guys i can only invite two people")
#
# # guest_removed0 = guest.pop(0)
# # print(f"\n hey {guest_removed0.title()} am sorry you are not invited")
# # guest_removed1 = guest.pop(0)
# # print(f"\n hey {guest_removed1.title()} am sorry you are not invited")
# # guest_removed2 = guest.pop(0)
# # print(f"\n hey {guest_removed2.title()} am sorry you are not invited")
# # guest_removed3 = guest.pop(0)
# # print(f"\n hey {guest_removed3.title()} am sorry you are not invited")
#
# # print(f"\n hey {guest[0].title()} you are still invited")
# # print(f"\n hey {guest[1].title()} you are still invited")
#
# # del guest[0]
# # del guest[0]
# # print(guest)
# # print(f"\n i am inviting {len(guest) }  people.")
# #
# # favorite = ["paris", "maldives", "nigeria", "dubai", "canada"]
# # print(favorite)
# # favorite.sort()
# #
# # favorite.reverse()
# #
# # favorite.reverse()
# #
# # favorite.sort()
# #
# # favorite.reverse()
# # print(favorite)
#
#
# pizzas = ["margarita", "seafood", "pepperoni", "chicken", "beef"]
# print("the first three items on the list are:")
# for pizza in pizzas[:3]:
#     print(pizza)
# print("\n")
# print("the last three items on the list are:")
# for pizza in pizzas[-3:]:
#     print(pizza)
# print("\n")
# print("the last three items from middle of  the list are:")
# for pizza in pizzas[1:4]:
#     print(pizza + "\n")
# friends_pizza = pizzas[:]
# pizzas.append("special")
# friends_pizza.append("mushroom")
# print("my favorite pizzas are:")
# for pizza in pizzas:
#     print(pizza)
print("\n")
print("my friends favorite pizzas are :")
for friends in friends_pizza:
    print(friends)
print("\n")

# tuples
foods = ("Salad", "chicken soup", "pasta", "afra", "benechin")
for food in foods:
    print(food)
foods = ("Salad", "chicken", "pasta", "afra", "benechin")
for food in foods:
    print(food)
print("\n")

# if statements
car = "sabaru"
if car.lower() == "sabaru":
    print("yayyyy")

age = 45
if age > 20 or age != 40:
    print("you're a kid")

alien_color = "yellow"
if alien_color == "green":
    print("you've earn yourself 5 points")
elif alien_color == "red":
    print("you've failed")
else:
    print("you've got yourself 10 points")



# for pizza in pizzas:
#     print(f"i like {pizza.title()} pizza")
# print("i really love pizza \n")
#
# Animals = ["dogs", "cats", "sheep"]
# for animal in Animals:
#     print(Animals)
age = 1
if age < 2:
    print("baby")
elif 2 >= age < 4:
    print("toddler")
elif 4 >= age < 13:
    print("kid")
elif 13 >= age < 20:
    print("teenager")
elif 20 >= age < 65:
    print("adult")
else:
    print("elder")

favorite_fruits = ["orange","banana","pineapple"]
if "apple " in favorite_fruits:
    print("you really love orange hehh")
else:
    print("please eat fruits")


