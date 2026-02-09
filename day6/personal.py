name = input("Enter your name: ")
goal = input("Enter your daily goal: ")

with open(r"C:\Users\Sanketreddy\Desktop\ERA\era-suprita-1\day6\journal.txt", "a") as file:
    file.write(name + " - " + goal + "\n")
