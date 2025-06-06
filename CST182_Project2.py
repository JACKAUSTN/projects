def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")

def add_contact(contact_book):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    if name in contact_book:
      print("Contact already exists!")
    else:
        contact_book[name] = {
	"phone": phone,
	"email": email,
	"address": address}   
        print("Contact added successfully!")
    
def view_contact(contact_book):
    name = input()
    if name in contact_book:
        print(f"Name: {name}")
        print(f"Phone: {contact_book[name]['phone']}")
        print(f"Email: {contact_book[name]['email']}")
        print(f"Address: {contact_book[name]['address']}")
    else:
        print("Contact not found!")

def edit_contact(contact_book):
    name = input()
    if name not in contact_book:
        print("Contact not found!")
    elif name in contact_book:
        phone = input()
        email = input()
        address = input()
        if phone == "":
            pass
        elif phone != "":
            contact_book[name]['phone'] = phone
        if email == "":
            pass
        elif email != "":
            contact_book[name]['email'] = email
        if phone == "":
            pass
        elif phone != "":
            contact_book[name]['phone'] = phone
        print("Contact updated successfully!")

def delete_contact(contact_book):
    name = input()
    if name not in contact_book:
        print("Contact not found!")
    elif name in contact_book:
        contact_book.pop(name)
        print("Contact deleted successfully!")

def list_all_contacts(contact_book):
    if not contact_book:
        print("No contacts available.")
    else:
        for name, details in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print("")


def new_func():
    return {}

contact_book = new_func()
# Contact Book Application
# This program allows users to manage a contact book with options to add, view, edit, delete, and list contacts.        


while True:
    display_menu()
    menu_choice = int(input("Enter your choice: "))
    if menu_choice == 1:
        add_contact(contact_book)
    elif menu_choice == 2:
        view_contact(contact_book)
    elif menu_choice == 3:
        edit_contact(contact_book)
    elif menu_choice == 4:
        delete_contact(contact_book)
    elif menu_choice == 5:
        list_all_contacts(contact_book)
    elif menu_choice == 6:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")

