class student:
    marks = [75, 82, 45, 90, 68]
    skills = {"Python", "SQL", "Git"}
    subjects = ("Python", "Django", "SQL")

    def display_marks(self):
        print("Student Marks:")
        for mark in self.marks:
            print(mark)

    def calculate_total(self):
        total = sum(self.marks)
        print("Total Marks:", total)

    def average(self):
        average = total / len (self.marks)
        print("Average Marks:")

        if average >= 50:
            print("Result: Pass")

        else:
            print("Result: Fail")



    






student = student()
student.display_marks()
student.calculate_total()
student.average()

