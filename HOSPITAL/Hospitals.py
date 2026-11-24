# Program that tells about main hospitals in iceland and give the info of the asked one.
import csv

print("Main Hospitals in Iceland:")
print()

# prints name of all hospitals. used "encoding="utf-8-sig" because .csv file was in icelandic characters. 
with open("Hospitals.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['id']},{row['name']}")

# asks for which hospital's info from given hospitals a user needs and provide
# location and specialty of that particular hospital.
with open("Hospitals.csv", "r", encoding="utf-8-sig") as views:
    analysing = csv.DictReader(views)
    print()
    info = input("which Hospital's info do you need?")
    for row in analysing:     
        if row['name'] == info or row['id'] == info:
            print(f"{info} is in {row['location']} & is specialised in {row['specialty']}")
            break
    else:
        print("Please Put correct information!!")
        
        