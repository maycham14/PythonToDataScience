class Guest:

    def __init__(self):
        self.filename = "guest.txt"

    def guest_list(self):

        while True:
            user = input("enter user name\nenter quit to exit.\n ")
            with open(self.filename, "a") as f:
                if user.lower() != "quit" or user.lower() != "q":
                    f.write(f"{user} \n")
                    self.read_file()
                else:
                    break

    def read_file(self):
        with open(self.filename) as file_objects:
            content = file_objects.read()
            print(content)


guest = Guest()
guest.guest_list()
