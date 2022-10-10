class InsertionSort:

    def sort(self, numbers):
        for i in range(1, len(numbers)):
            value = numbers[i]
        while numbers[i] > value and i > 0:
            numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
            i -= 1
        print(numbers)




insert = InsertionSort()
num = [2, 2, 3, 1, 1, 45, 65, 33, 11]
insert.sort(num)
