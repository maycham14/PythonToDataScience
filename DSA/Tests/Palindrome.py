class Palindrome:

    def palindrome(self,word):

        if word == word[::-1]:
            print(f"{word} is a palindrome")
        else:
            print(f"{word} is not a palindrome")


checker = Palindrome()
checker.palindrome("waw")