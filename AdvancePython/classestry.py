class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def open_restaurant(self):
        print(f"the {self.restaurant_name} is open")

    def describe_restaurant(self):
        print(f"the {self.restaurant_name} is beautiful")
        print(f"the restaurant is {self.cuisine_type} ")

    def set_number_served(self, number):
        self.number_served = number
        print(f"the number of served customers are {self.number_served}")

    def increment_number_served(self, number):
        self.number_served += number
        print(f"the number of served customers is {self.number_served}")


rest = Restaurant("ali baba", "chinese")
rest.describe_restaurant()
rest.set_number_served(23)
rest.increment_number_served(3455)
rest.increment_number_served(234)
