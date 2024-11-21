# contact_book.py

contacts = []

def add_contact(name, phone, email, address):
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact(search_term):
    found_contacts = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]
    if not found_contacts:
        print("No contacts found.")
    else:
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

def update_contact(name, new_phone=None, new_email=None, new_address=None):
    for contact in contacts:
        if contact['name'] == name:
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            if new_address:
                contact['address'] = new_address
            print(f"Contact '{name}' updated.")
            return
    print("Contact not found.")

def delete_contact(name):
    global contacts
    contacts = [contact for contact in contacts if contact['name'] != name]
    print(f"Contact '{name}' deleted.")

def main():
    print("Contact Book!")
    
    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone, email, address)
            print("Contact added.")
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            search_contact(search_term)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_phone = input("Enter new phone number (leave blank to skip): ")
            new_email = input("Enter new email (leave blank to skip): ")
            new_address = input("Enter new address (leave blank to skip): ")
            update_contact(name, new_phone, new_email, new_address)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(name)
        elif choice == '6':
            print("Exiting the Contact Book.")
            break
        else:
            print(" Invalid!! Please try again.")

if __name__ == "__main__":
    main()
