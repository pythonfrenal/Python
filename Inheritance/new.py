class Mother:
    def cook (self):
        print("cooking.")

class Father:
    def swim(self):
        print("swimming.")

class chiled (Mother,Father):
    pass

c=chiled()

c.cook()
c.swim()
