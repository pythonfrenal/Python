# Decorator
def student_report(func):
    def wrapper(self):
        print("--- Student Report ---")
        func(self)
    return wrapper


# Student class
class Student:

    marks = [75, 82, 45, 90, 68]

    def total_marks(self):
        return sum(self.marks)

    def average_marks(self):
        return sum(self.marks) / len(self.marks)

    @student_report
    def report(self):

        # Calculate total
        total = self.total_marks()

        # Calculate average
        average = self.average_marks()

        print("Marks:")

        # Print each mark using for loop
        for mark in self.marks:
            print(mark)

        print("Total:", total)
        print("Average:", average)

        # Pass or Fail
        if average >= 50:
            print("Result: Pass")
        else:
            print("Result: Fail")

        # Lambda function to find highest mark
        highest = lambda marks: max(marks)
        print("Highest Mark:", highest(self.marks))


# Create object
student = Student()

# Display report
student.report()