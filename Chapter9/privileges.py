class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges include: ")
        for p in self.privileges:
            print(p)