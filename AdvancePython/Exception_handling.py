class Exception:

    def addition(self):
        while True:
            num1 = input("enter a number:\n")
            num2 = input("enter a number:\n")

            try:
                answer = int(num1) + int(num2)
            except ValueError:
                print("your inputs should be only numbers")
            else:
                print(f"the answer is \t{answer}")


exception = Exception()
exception.addition()
