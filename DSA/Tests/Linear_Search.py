class LinearSearch:

    def search(self, target, datas):
        length = len(datas)
        i = 0
        while i < length:
            if target == datas[i]:
                return True
            else:
                return False
        i += 1

    def search1(self, target, datas):
        for data in datas:
            if target == data:
                return True
        else:
            return False


checker = LinearSearch()
numbers = [3, 4, 5, 1, 2, 3]
print(checker.search(3, numbers))
print(checker.search1(5, numbers))
