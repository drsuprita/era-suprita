import csv

with open("C:\\Users\\Sanketreddy\\Desktop\\ERA\\era-suprita-1\\day6\\student.csv", "r") as file:
    reader = csv.DictReader(file) 

    print("Students who Passed:\n")

    for row in reader:
        if row["Status"] == "Pass":
            print(row["Name"])