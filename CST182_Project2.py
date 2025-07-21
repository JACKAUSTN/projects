# Contact Book - Personal Management Tool
# CST182.2 Project 2

def save_contacts_to_file(contact_book):
    file = open("my_contacts.txt", "w")
    for name in contact_book:
        file.write(name + "\n")
        file.write(contact_book[name]["phone"] + "\n")
        file.write(contact_book[name]["email"] + "\n")
        file.write(contact_book[name]["address"] + "\n")
        file.write("---\n")
    file.close()
    print("Contacts saved to file!")

def load_contacts_from_file():
    contact_book = {}
    try:
        file = open("my_contacts.txt", "r")
        lines = file.readlines()
        file.close()
        
        i = 0
        while i < len(lines):
            if i + 3 < len(lines):
                name = lines[i].strip()
                phone = lines[i + 1].strip()
                email = lines[i + 2].strip()
                address = lines[i + 3].strip()
                
                contact_book[name] = {
                    "phone": phone,
                    "email": email,
                    "address": address
                }
                i = i + 5
            else:
                break
        print("Contacts loaded from file!")
    except FileNotFoundError:
        print("No existing contacts file found. Starting fresh!")
    
    return contact_book

def display_menu():
    print("\n" + "="*30)
    print("    CONTACT BOOK MENU")
    print("="*30)
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Search Contacts")
    print("7. Save & Exit")
    print("="*30)

def add_contact(contact_book):
    print("\n--- Adding New Contact ---")
    name = input("Enter contact name: ")
    
    name = name.title()
    
    if name in contact_book:
        print("Contact already exists!")
        return
    
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    
    if name == "" or phone == "":
        print("Name and phone number are required!")
        return
    
    contact_book[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }   
    print("Contact added successfully!")
    
def view_contact(contact_book):
    print("\n--- View Contact ---")
    name = input("Enter contact name to view: ")
    name = name.title()
    
    if name in contact_book:
        print("\n" + "-"*25)
        print(f"Name: {name}")
        print(f"Phone: {contact_book[name]['phone']}")
        print(f"Email: {contact_book[name]['email']}")
        print(f"Address: {contact_book[name]['address']}")
        print("-"*25)
    else:
        print("Contact not found!")

def edit_contact(contact_book):
    print("\n--- Edit Contact ---")
    name = input("Enter contact name to edit: ")
    name = name.title()
    
    if name not in contact_book:
        print("Contact not found!")
        return
    
    print("Leave blank to keep current value")
    print(f"Current phone: {contact_book[name]['phone']}")
    phone = input("Enter new phone number: ")
    
    print(f"Current email: {contact_book[name]['email']}")
    email = input("Enter new email address: ")
    
    print(f"Current address: {contact_book[name]['address']}")
    address = input("Enter new address: ")
    
    if phone != "":
        contact_book[name]['phone'] = phone
    if email != "":
        contact_book[name]['email'] = email
    if address != "":
        contact_book[name]['address'] = address
        
    print("Contact updated successfully!")

def delete_contact(contact_book):
    print("\n--- Delete Contact ---")
    name = input("Enter name of contact to delete: ")
    name = name.title()
    
    if name not in contact_book:
        print("Contact not found!")
        return
    
    confirm = input(f"Are you sure you want to delete {name}? (yes/no): ")
    if confirm.lower() == "yes" or confirm.lower() == "y":
        contact_book.pop(name)
        print("Contact deleted successfully!")
    else:
        print("Delete cancelled.")

def list_all_contacts(contact_book):
    print("\n--- All Contacts ---")
    if not contact_book:
        print("No contacts available.")
        return
    
    names = sorted(contact_book.keys())
    
    contact_number = 1
    for name in names:
        details = contact_book[name]
        print(f"\n{contact_number}. {name}")
        print(f"   Phone: {details['phone']}")
        print(f"   Email: {details['email']}")
        print(f"   Address: {details['address']}")
        contact_number = contact_number + 1

def search_contacts(contact_book):
    print("\n--- Search Contacts ---")
    search_term = input("Enter name or phone to search: ")
    search_term = search_term.lower()
    
    found_contacts = []
    
    for name in contact_book:
        if search_term in name.lower() or search_term in contact_book[name]['phone']:
            found_contacts.append(name)
    
    if len(found_contacts) == 0:
        print("No contacts found matching your search.")
    else:
        print(f"Found {len(found_contacts)} contact(s):")
        for name in found_contacts:
            details = contact_book[name]
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")

# Main program starts here
print("Welcome to Your Personal Contact Book!")
contact_book = load_contacts_from_file()

running = True
while running:
    display_menu()
    
    try:
        menu_choice = int(input("\nEnter your choice (1-7): "))
    except:
        print("Please enter a valid number!")
        continue
    
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
    search_contacts(contact_book)
elif menu_choice == 7:
    save_contacts_to_file(contact_book)
    print("Thank you for using Contact Book!")
    print("Program ended.")
    running = False
else:
    print("Invalid choice. Please try again.")