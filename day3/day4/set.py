fruits = {"apple", "banana", "orange", "apple"}
print(fruits)
fruits.add("mango")
fruits.remove("banana")   # error if not found
fruits.discard("grape")   # no error if not found
for fruit in fruits:
    print(fruit)

A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)
print(A & B)
print(A - B)

