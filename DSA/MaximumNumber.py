class Maximum:

    def maximum_number(self, datas):
        maximum_value = datas[0]
        for data in datas:
            if data > maximum_value:
                maximum_value = data
        print(f"the maximum_number is {maximum_value}")

    def minimum_number(self, datas):
        minimum_number = datas[0]
        for data in datas:
            if data < minimum_number:
                minimum_number = data


maxi = Maximum()
lists = [1, 45, 76, 89, 65]
maxi.maximum_number(lists)
maxi.minimum_number(lists)
