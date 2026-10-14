# Delete the file after confirmation using os.remove().

import os

filename = input("Enter the file name to delete: ")

if os.path.exists(filename):
    confirm = input("Are you sure you want to delete this file? (yes/no): ")

    if confirm.lower() == "yes":
        os.remove(filename)
        print("File deleted successfully.")
    else:
        print("File was not deleted.")
else:
    print("File not found.")
    