class Mother:

    def cook(self):
        print("Cooking.")


class Father:

    def drive(self):
        print("Driving.")


class Child(Mother, Father):

    pass


c = Child()

c.cook()
c.drive()