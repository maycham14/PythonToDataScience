username = ["admin", "phoenix", "blaqfire", "maycham"]
for user in username:
    print(f"welcome {user}")
for user in username:
    if user == "admin":
        print(f"hello {user} would you like to see a status report.\n")
    else:
        print(f"welcome {user}.\n")

del username[0]
del username[0]
del username[0]
del username[0]

if username:
    for user in username:
        print(f"users are {user}")
else:
    print("we need to find some users")

current_users = ["sibo", "may", "amadu", "lie john", "mariama", "binta."]
new_users = ["juwara", "sibo", "amadu", "juksin"]

for user in current_users:
    if user in new_users:
        print(f"please {user} is already taken.\n")
    else:
        print(f"user name {user} is available.\n")

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in data:
    if i == 1:
        print(f"{i}st")
    elif i == 2:
        print(f"{i}nd")
    elif i == 3:
        print(f"{i}rd")
    else:
        print(f"{i}th")
