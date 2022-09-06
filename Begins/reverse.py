def reverse_numbers():
    numbers = []
    for i in range(1, 4):
        i = int(input("enter a number:\n"))
        numbers.append(i)

    print(numbers)


def reverse():
    number = int(input("enter a number:\n"))
    rev = int(str(number)[::-1])
    print(rev)


reverse_numbers()
reverse()
