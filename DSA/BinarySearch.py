class BinarySearch:

    def binary_search(self, target, low, high, data):
        mid = (low + high) // 2
        if low > high:
            return False
        elif target == data[mid]:
            return True
        elif target < data[mid]:
            return self.binary_search(target, low, mid - 1, data)
        else:
            return self.binary_search(target, mid + 1, high, data)


binary = BinarySearch()
data = [1, 2, 3, 4, 5]
print(binary.binary_search(5, 0, 4, data))
