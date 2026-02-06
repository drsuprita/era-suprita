person = {"name": "Suprita", "age": 21, "city": "athani"}

age = person.pop("age")
print(age)      
print(person)   

person = {"name": "Suprita", "age": 21}

item = person.popitem()
print(item)    
print(person)   

colors = {"red", "blue", "green"}

colors.remove("blue")
print(colors)

colors = {"red", "blue", "green"}

colors.discard("yellow")   
print(colors)

student = {
    "name": "Suprita",
    "age": 22,
    "course": "Python"
}
for key in student:
    print(key)
for value in student:
    print(student[value])
print(student)
for key, value in student.items():
    if key == "age":
        print("Age is", value)
        marks = {"Math": 80, "Science": 75, "English": 85}

for subject in marks:
    marks[subject] += 5

print(marks)