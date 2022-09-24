class Animals:
    def my_pets(self):
        self.filename =["Cat.txt","Dogs.txt"]
        try:

            with open(self.filename) as file_objects:
                for i in self.filename:
                     i = file_objects.read()
        except FileNotFoundError:
            print("cannot locate this file")
        else:
            print(i)


animal = Animals()
animal.my_pets()