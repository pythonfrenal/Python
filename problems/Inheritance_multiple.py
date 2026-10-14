class mother:
    def cook(self):
        print("cooking.")

class father:
    def drive(self):
        print("driving.")

class chiled(mother,father):
    pass

c=chiled()
c.cook()
c.drive()

