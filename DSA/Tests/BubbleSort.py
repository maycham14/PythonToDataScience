class BubbleSort:

    def sort(self, lists):
        for i in range(len(lists) - 1, 0, -1):
            for j in range(i):
                if lists[j] > lists[j + 1]:
                    temp = lists[j]
                    lists[j] = lists[j + 1]
                    lists[j + 1] = temp
        print(lists)


bubble_sorting = BubbleSort()
numbers = [3, 2, 5, 4, 67, 32, 88, 43, 99]
bubble_sorting.sort(numbers)
