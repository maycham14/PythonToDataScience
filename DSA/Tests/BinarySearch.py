class BinarySearch:

    def __init__(self):
        self.low = None
        self.high = None

    def binary_search(self, target, low, high, data):
        mid = (high + low) // 2
        if low > high or target > data[high] or target < data[low]:
            return False
        elif data[mid] == target:
            return True
        elif target > data[mid]:
            return self.binary_search(target, mid + 1, high, data)
        elif target < data[mid]:
            return self.binary_search(target, low, mid - 1, data)

    # def binary(self, datas, target):
    #     self.high = (len(datas) - 1)
    #     self.low = 0
    #     mid = (self.high + self.low) // 2
    #     if self.low > self.high or target > datas[self.high] or target < datas[self.low]:
    #         return False
    #     elif datas[mid] == target:
    #         return True
    #     elif target > datas[mid]:
    #         self.low = mid + 1
    #         return self.binary(datas, target)
    #     elif target < datas[mid]:
    #         self.high = mid - 1
    #         return self.binary(datas, target)


search = BinarySearch()
numbers = [2, 3, 5, 6, 7, 8]
print(search.binary_search(9, 0, 5, numbers))
# print(search.binary(numbers, 8))
