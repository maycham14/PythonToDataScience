import json


class Favoritenumber:

    def add_num(self):
        filename = "Favorite_number.json"
        try:
            with open(filename) as f:
               file = json.load(f)
        except FileNotFoundError:
            file = int(input("enter your favorite number:\n"))
            with open(filename, "a") as f:
                json.dump(file,f)
                print(f"your favorite number is {file}")

        else:
            print(f"yor favorite number is {file}")



favorite = Favoritenumber()
favorite.add_num()
