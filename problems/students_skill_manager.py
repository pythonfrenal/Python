# Create a class Student with:
# python
# skills = {"Python", "SQL", "Git"}
# subjects = ("Python", "Django", "SQL")
# Create methods to:
# - Display all skills using a for loop.
# - Add a new skill.
# - Check whether "Python" is present in the skills set.
# - Display all subjects using a for loop.
# - Display the total number of skills and subjects.

class Student:

    skills = {"Python", "SQL", "Git"}
    subjects = ("Python", "Django", "SQL")

    # Display all skills
    def display_skills(self):
        print("Skills:")
        for skill in self.skills:
            print(skill)

    # Add a new skill
    def add_skill(self, skill):
        self.skills.add(skill)
        print("\nNew skill added:", skill)

    # Check whether Python is present
    def check_python(self):
        if "Python" in self.skills:
            print("\nPython is present in skills.")
        else:
            print("\nPython is not present in skills.")

    # Display all subjects
    def display_subjects(self):
        print("\nSubjects:")
        for subject in self.subjects:
            print(subject)

    # Display total number of skills and subjects
    def display_total(self):
        print("\nTotal number of skills:", len(self.skills))
        print("Total number of subjects:", len(self.subjects))


# Create object
student = Student()

student.display_skills()

student.add_skill("Django")

student.check_python()

student.display_subjects()

student.display_total()
