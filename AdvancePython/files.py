class Files:
    def __init__(self):
        self.filename = "learning_python.txt"

    def read_file(self):
        with open(self.filename) as file_objects:
            content = file_objects.read()
            print(content)

    def reading_by_line(self):
        with open(self.filename) as file_objects:
            for file_object in file_objects:
                print(file_object.rstrip())

    def lines_in_list(self):
        with open(self.filename) as file_objects:
            lines = file_objects.readline()
        for line in lines:
            print(line.rstrip())

    # def replacing_words(self):
    #     with open(self.filename) as file_objects:
    #         file_objects.replace('python', 'java')
    #         content = file_objects.readline()
    #
    #         print(content)

    # writing to a file
    def write_to_file(self):
        with open(self.filename, "a") as file_objects:
            while True:
                request = input("please enter your:")
                if request.lower() == quit:
                    break
                else:
                    file_objects.write(request)

        print(file_objects)


file = Files()
file.read_file()
file.reading_by_line()
file.lines_in_list()
file.write_to_file()
