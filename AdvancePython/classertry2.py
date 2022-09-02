from classestry import Restaurant


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["chocolate", "vanilla", "orange", "coffee"]

    def ice_cream_flavors(self):
        for i in self.flavors:
            print(f"flavors are {i}")


my = IceCreamStand("place", "gambian")
print(my.describe_restaurant())
my.ice_cream_flavors()
