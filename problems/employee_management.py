# Employee Management
# Create a class Employee with:
# python
# employees = {
#     "Rahul": 25000,
#     "Anu": 35000,
#     "John": 45000,
#     "Meera": 28000
# }
# Create methods to:
# - Display all employees and their salaries using a for loop.
# - Find the total salary.
# - Calculate the average salary.
# - Display employees earning more than 30000.
# - Store the departments in a tuple:
# python
# departments = ("IT", "HR", "Finance")
# - Store unique employee skills in a set and display them.


class Employee:

    employees = {
        "Rahul": 25000,
        "Anu": 35000,
        "John": 45000,
        "Meera": 28000
    }

    departments = ("IT", "HR", "Finance")

    skills = {"Python", "SQL", "Git", "Excel"}

    # Display all employees and salaries
    def display_employees(self):
        print("Employees and Salaries:")
        for name, salary in self.employees.items():
            print(name, ":", salary)

    # Find total salary
    def total_salary(self):
        total = 0

        for salary in self.employees.values():
            total += salary

        print("\nTotal Salary:", total)
        return total

    # Calculate average salary
    def average_salary(self):
        total = self.total_salary()
        average = total / len(self.employees)

        print("Average Salary:", average)
        return average

    # Display employees earning more than 30000
    def high_salary_employees(self):
        print("\nEmployees earning more than 30000:")

        for name, salary in self.employees.items():
            if salary > 30000:
                print(name, ":", salary)

    # Display departments
    def display_departments(self):
        print("\nDepartments:")

        for department in self.departments:
            print(department)

    # Display unique skills
    def display_skills(self):
        print("\nUnique Employee Skills:")

        for skill in self.skills:
            print(skill)


# Create object
employee = Employee()

employee.display_employees()
employee.average_salary()
employee.high_salary_employees()
employee.display_departments()
employee.display_skills()
