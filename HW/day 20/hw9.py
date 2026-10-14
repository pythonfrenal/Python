class Employee:
    def __init__(self, salary):
        self.salary = salary

    def display_salary(self):
        print("Salary:", self.salary)


class Manager(Employee):
    def manage(self):
        print("Manager manages the team")


# Create Manager object
m = Manager(50000)

m.display_salary()
m.manage()
