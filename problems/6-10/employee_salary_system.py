# Parent class
class Employee:

    def calculate_salary(self, salary):
        try:
            salary = float(salary)

            if salary < 0:
                raise ValueError("Salary cannot be negative.")

            # Lambda function to increase salary by 10%
            increase_salary = lambda amount: amount * 1.10

            return increase_salary(salary)

        except (ValueError, TypeError) as e:
            print("Invalid salary:", e)
            return 0


# Child class
class Developer(Employee):

    def display_salary_details(self, name, salary):
        try:
            final_salary = self.calculate_salary(salary)

            print("Name:", name)
            print("Original Salary:", salary)
            print("Final Salary:", final_salary)

        except Exception as e:
            print("Error:", e)


# Employee data
employees = [
    {"name": "Rahul", "salary": 30000},
    {"name": "Anu", "salary": 45000},
    {"name": "John", "salary": 55000}
]


# Store employee names in a set
employee_names = set()

# Store salary levels in a tuple
salary_levels = ("Low", "Medium", "High")


# Create Developer object
developer = Developer()


# Display employees using for loop
print("Employee Details:")
for employee in employees:

    name = employee["name"]
    salary = employee["salary"]

    employee_names.add(name)

    print("\nName:", name)
    print("Salary:", salary)

    # Check salary greater than 40000
    if salary > 40000:
        print("Salary is greater than 40000")
    else:
        print("Salary is 40000 or less")


# Display employee names
print("\nEmployee Names:", employee_names)

# Display salary levels
print("Salary Levels:", salary_levels)


# Display final salary details
print("\n--- Final Salary Details ---")

for employee in employees:
    developer.display_salary_details(
        employee["name"],
        employee["salary"]
    )