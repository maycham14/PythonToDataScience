def show_messages(people):
    while people:
        current = people.pop()
        print(f"before popping {current}")
        peoples.append(current)


def send_messages(peoples):
    for p in peoples:
        print(f" after popping {p}")


people = ["may", "tima", "sira"]
peoples = []
show_messages(people)
send_messages(peoples[:])
