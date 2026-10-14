
class Employee:
    def __init__(self, salary):
        self.__salary = 0
        self.set_salary(salary)

    # Set the salary
    def set_salary(self, salary):
        if salary <= 0:
            raise ValueError("Salary must be greater than zero!")
        self.__salary = salary

    # Get the salary
    def get_salary(self):
        return self.__salary

    # Calculate annual salary
    def calculate_annual_salary(self):
        return self.__salary * 12


class Developer(Employee):
    def __init__(self, salary):
        super().__init__(salary)
        self.skills = {"Python", "Django", "SQL"}

    def display_skills(self):
        print("Developer Skills:")
        for skill in self.skills:
            print(skill)

    def add_skill(self, skill):
        self.skills.add(skill)
        print("New skill added:", skill)


# Main program with error handling
try:
    salary = float(input("Enter monthly salary: "))

    developer = Developer(salary)

    print("Monthly Salary:", developer.get_salary())
    print("Annual Salary:", developer.calculate_annual_salary())

    developer.display_skills()

    new_skill = input("Enter a new skill: ")
    developer.add_skill(new_skill)

    print("Updated Skills:", developer.skills)

except ValueError as e:
    print("Invalid salary input:", e)
