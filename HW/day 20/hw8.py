class Bird:
    def fly(self):
        print("Bird can fly")


class Penguin(Bird):
    def fly(self):
        print("Cannot fly")


# Create object of Penguin
p = Penguin()
p.fly()
