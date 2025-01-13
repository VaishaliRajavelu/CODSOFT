contacts={}
def addcontact():
    name=input("enter the name").strip()
    phone=input("enter the phone number").strip()
    address=input("enter the address").strip()
    email=input("enter the email").strip()
    
    if name in contacts:
        print("already exists")
    else:
        contacts[name]={"Phone":phone,
                        "Email":email,
                        "Address":address}
        print(name,"added successfully")

def viewcontacts():
    if contacts:
        print("\nContact List:")
        for name,details in contacts.items():
            print(f"- {name}: {details['Phone']}")
    else:
        print("No contacts available.")

def searchcontact():
    query=input("Enter name or phone number to search: ").strip()
    found=False
    for name,details in contacts.items():
        if query.lower() in name.lower() or query==details['Phone']:
            print(f"\nContact Found:\nName: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
            found=True
    if not found:
        print("No contact found")

def updatecontact():
    name=input("Enter the name of the contact to update: ").strip()
    if name in contacts:
        print(f"Current Details: {contacts[name]}")
        phone=input("Enter new phone number: ").strip()
        email=input("Enter new email: ").strip()
        address=input("Enter new address: ").strip()

        if phone:
            contacts[name]['Phone']=phone
        if email:
            contacts[name]['Email']=email
        if address:
            contacts[name]['Address']=address
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"No contact found with the name '{name}'.")

def deletecontact():
    name=input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"No contact found with the name '{name}'.")

def main():
    while True:
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice=input("Enter your choice (1-6): ").strip()

        if choice=='1':
            addcontact()
        elif choice=='2':
            viewcontacts()
        elif choice=='3':
            searchcontact()
        elif choice=='4':
            updatecontact()
        elif choice=='5':
            deletecontact()
        elif choice=='6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()

    

    


    


    
