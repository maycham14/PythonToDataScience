class BubbleSort:

    def sort(self, numbers):
        for i in range(len(numbers) - 1, 0, -1):
            for j in range(i):
                if numbers[j] > numbers[j+1]:
                    temp = numbers[j]
                    numbers[j] = numbers[j+1]
                    numbers[j + 1] = temp
        print(numbers)


num = [2, 4, 1, 6, 7]
output = BubbleSort()
output.sort(num)
