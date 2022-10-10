class LinearSearch:

    def linear_search(self, target, data):
        length = len(data)
        i = 0
        while i < length:
            if data[i] == target:
                return True
            i += 1

        return False


linear = LinearSearch()
numbers = [1, 2, 4, 5, 6]
print(linear.linear_search(0, numbers))


