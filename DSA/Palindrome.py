class Palindrome:

    def isPalindrome(self, word):
        if word == word[::-1]:
            print("is a palindrome")
        else:
            print("is not a palindrome")


palindrome = Palindrome()
palindrome.isPalindrome("hay")
