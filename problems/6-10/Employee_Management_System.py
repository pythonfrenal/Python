# Parent class
class Employee:

    def display_details(self):
        print("Name:", employee["name"])
        print("Salary:", employee["salary"])
        print("Department:", employee["department"])


# Child class
class Manager(Employee):

    skills = {"Python", "SQL", "Leadership"}

    department_history = ("HR", "Finance", "IT")

    # Method to add a new skill
    def add_skill(self, skill):
        self.skills.add(skill)
        print("New skill added:", skill)

    # Method to display skills
    def display_skills(self):
        print("\nSkills:")
        for skill in self.skills:
            print(skill)


# Employee dictionary
employee = {
    "name": "Rahul",
    "salary": 50000,
    "department": "IT"
}


# Create Manager object
manager = Manager()

# Display employee details
manager.display_details()

# Display skills
manager.display_skills()

# Display department history
print("\nDepartment History:", manager.department_history)

# Check salary
if employee["salary"] > 40000:
    print("\nSalary is greater than 40000")
else:
    print("\nSalary is 40000 or less")

# Add new skill
manager.add_skill("Django")

# Display updated skills
manager.display_skills()