
marks = []

def get_marks():
    subjects = ["English", "Maths", "Science", "Social", "Computer"]

    for subject in subjects:
        mark = int(input("Enter " + subject + " marks: "))
        marks.append(mark)


def calculate_total():
    return sum(marks)


def calculate_average():
    return calculate_total() / len(marks)


def find_grade():
    average = calculate_average()

    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "Fail"


def display_result():
    total = calculate_total()
    average = calculate_average()
    grade = find_grade()

    print("\n--- Student Result ---")
    print("Total Marks :", total)
    print("Average     :", round(average))
    print("Grade       :", grade)

    if all(mark >= 50 for mark in marks):
        print("Result      : PASS")
    else:
        print("Result      : FAIL")


# Main program
get_marks()
display_result()
