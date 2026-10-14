
class Student:
    def __init__(self):
        self.marks = [75, 82, 45, 90, 68]
        self.skills = {"Python", "SQL", "Git"}
        self.subjects = ("Python", "Django", "SQL")

    def report(self):
        # Display marks using a for loop
        print("Student Marks:")
        for mark in self.marks:
            print(mark)

        # Calculate total and average
        total = sum(self.marks)
        average = total / len(self.marks)

        print("Total Marks:", total)
        print("Average Marks:", average)

        # Check Pass or Fail
        if average >= 50:
            print("Result: Pass")
        else:
            print("Result: Fail")

        # Add a new skill
        self.skills.add("Django")
        print("Skills:", self.skills)

        # Display subjects
        print("Subjects:")
        for subject in self.subjects:
            print(subject)

        # Find highest mark using lambda
        highest = lambda marks: max(marks)
        print("Highest Mark:", highest(self.marks))

        # Nested function to count skills
        def skill_count():
            return len(self.skills)

        print("Number of Skills:", skill_count())


# Create an object
student1 = Student()

# Display student report
student1.report()
