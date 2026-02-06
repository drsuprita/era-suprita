contacts = {
    "Amit": "9876543210",
    "Priya": "9123456780",
    "Rahul": "9988776655"
}

contacts["Sneha"] = "9090909090"
contacts["Priya"] = "9000011111"

print("Safe Lookups")
print("----------------")
print("Amit:", contacts.get("Amit", "Contact not found"))       
print("Karan:", contacts.get("Karan", "Contact not found"))      

print("\nAll Contacts")
print("----------------")

for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")