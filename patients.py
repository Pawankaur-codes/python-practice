# The code that asks info of patients such as their name,age and save it to a file.

import csv # (comma seperate value file)

print("write DONE to break the loop.")

while True:
    name = input("What is your name? ")
    if name == "DONE": # asks until user writes DONE.
        break
    age = input("How old are you? ")
    illness = input("what illness do you have? ")

    with open("patient.csv", "a", newline="") as file:
        writes = csv.DictWriter(file, fieldnames=["name", "age", "illness"])
        writes.writerow({"name":name, "age":age, "illness":illness})
        
print("The data have been recorded.")
