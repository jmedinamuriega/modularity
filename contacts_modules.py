import contacts_manager

def contacts():
    contacts = {}
    while True:
        print('''This is the contact manager
                    1) Add a contact
                    2) Display all contacts
                    3) Remove a contact
                    4)quit''')
        choice = input("Select an option: ")
        if choice == "1":
            name = input("Please introduce the name: ")
            number = input("Please introduce the phone number: ")
            email = input("Please introduce the email address: ")
            birthday = input("Please introduce the birthday: ")
            contacts_manager.add_contact(name, number, email, birthday, contacts)
        elif choice == "2":
            contacts_manager.view_contacts(contacts)
        elif choice =="3":
            name = input("What contact do you want to delete? ")
            contacts_manager.delete_contact(name,contacts)
        elif choice=="4":
            break
contacts()