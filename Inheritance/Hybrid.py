class GrandFather:

    def grand_father_feature(self):
        print("Grandfather: Wise and experienced")


class Father(GrandFather):

    def father_feature(self):
        print("Father: Hardworking and caring")


class Aunt(GrandFather):

    def aunt_feature(self):
        print("Aunt: Kind and supportive")


class Child(Father, Aunt):

    def child_feature(self):
        print("Child: Energetic and curious")


# Creating object of Child
c = Child()

c.grand_father_feature()
c.father_feature()
c.aunt_feature()
c.child_feature()