degrees = int(input("please enter a number:\n"))
choices = input("enter c to convert to celsius or enter f to convert to fahrenheit.\n")

if choices.lower() == "c":
    print(f"{degrees} to celsius is :\n")
    value0 = (degrees-32) * 5/9
    print(str(value0.__round__()) + "\n" + "degree celsius")
elif choices.lower() == "f":
    print(f"{degrees} celsius to fahrenheit is :\n")
    value = (degrees-32) * 5/9
    print(str(value.__round__())+"\n" + "degree fahrenheit")