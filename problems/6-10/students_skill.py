# Decorator
def student_report_decorator(func):
    def wrapper(self):
        print("--- Student Report Started ---")

        func(self)

        print("--- Student Report Completed ---")

    return wrapper


# Student class
class Student:

    skills = {"Python", "SQL", "Git"}

    subjects = ("Python", "Django", "Machine Learning")

    @student_report_decorator
    def student_report(self):

        # Display skills
        print("\nSkills:")
        for skill in self.skills:
            print(skill)

        # Display subjects
        print("\nSubjects:")
        for subject in self.subjects:
            print(subject)

        # Check whether Python is present
        if "Python" in self.skills:
            print("\nPython is present in skills.")
        else:
            print("\nPython is not present in skills.")

        # Nested function
        def skill_count():
            return len(self.skills)

        print("Number of skills:", skill_count())


# Create object
student = Student()

# Call report
student.student_report()