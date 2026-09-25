try:
    file = open("D:\\python full stack\\python\\Inheritance\\problems\\day 18\\data.txt", "r")

    content = file.read()

    print(content)

    file.close()

except FileNotFoundError:
    print("File not found!")