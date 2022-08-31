class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def open_restaurant(self):
        print(f"the {self.restaurant_name} is open")

    def describe_restaurant(self):
        print(f"the {self.restaurant_name} is beautiful")
        print(f"the restaurant is {self.cuisine_type} ")


rest = Restaurant("ali baba", "chinese")
info = Restaurant("ali abdul", "arabian")
info2 = Restaurant("ali rasheed", "asian")
rest.open_restaurant()
rest.describe_restaurant()
info.describe_restaurant()
info2.describe_restaurant()
