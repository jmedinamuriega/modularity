def add_contact(name, number, email, birthday, contacts):
    contacts[name] = {"Phone Number": number, "Email Address": email,"Birthday":birthday}
def view_contacts(contacts):
    for name, details in contacts.items():
        for key, value in details.items():
            print(f"{key}: {value}")
        print()    
def delete_contact(name, contacts):
    if name in contacts:
        del contacts[name]
        print(f"The contact {name} has been deleted.")
    else:
        print("The contact does not exist.")
