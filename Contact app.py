contacts = []

print("=== Contact App ===")
print("1. Add Contact")
print("2. View Contact")
print("3. Remove Contact")

choice = input("Choose an option (1-3): ")

if choice == "1":
name = input("Enter name: ")
phone = input("Enter phone number: ")
contacts.append([name, phone])
print("Contact added:", name, "-", phone)

elif choice == "2":
if len(contacts) == 0:
print("No contacts saved.")
elif len(contacts) == 1:
print("Contact:", contacts[0][0], "-", contacts[0][1])
elif len(contacts) == 2:
print("Contact 1:", contacts[0][0], "-", contacts[0][1])
print("Contact 2:", contacts[1][0], "-", contacts[1][1])
else:
print("Too many contacts to show simply!")

elif choice == "3":
if len(contacts) == 0:
print("No contacts to remove.")
elif len(contacts) == 1:
name = input("Enter name to remove: ")
if name == contacts[0][0]:
contacts.pop(0)
print("Contact removed:", name)
else:
print("Name not found.")
elif len(contacts) == 2:
name = input("Enter name to remove: ")
if name == contacts[0][0]:
contacts.pop(0)
print("Contact removed:", name)
elif name == contacts[1][0]:
contacts.pop(1)
print("Contact removed:", name)
else:
print("Name not found.")
else:
print("Too many contacts to remove simply!")

else:
print("Invalid choice.")
