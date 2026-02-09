file = None
try:
    file = open("day6/test.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found. Please open an existing file.")
finally:
    if file:
        file.close()
        print("File was closed.")
