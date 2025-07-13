# Initialize an empty dictionary to store contacts
contacts = {}

# Infinite loop to keep the app running until the user chooses to exit
while True:
    # Display menu options to the user
    print("\nContact Book App")
    print("1. Create contact")
    print("2. View contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Search contact")
    print("6. Count contacts")
    print("7. Exit")

    # Get the user's choice
    choice = input("Enter your choice : ")

    # Create a new contact
    if choice == '1':
        name = input("Enter your name : ")
        if name in contacts:
            print(f'Contact name {name} already exists ')
        else:
            age = input("Enter age : ")
            email = input("Enter email : ")
            mobile = input("Enter mobile number : ")
            # Store contact details as a nested dictionary
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f"Contact name {name} has been created successfully")

    # View an existing contact
    elif choice == '2':
        name = input("Enter contact name to view : ")
        if name in contacts:
            contact = contacts[name]
            # Corrected the output to use values from the contact dictionary
            print(f'Name: {name}, Age: {contact["age"]}, Mobile Number: {contact["mobile"]}, Email: {contact["email"]}')
        else:
            print('Contact is not found')

    # Update an existing contact
    elif choice == '3':
        name = input("Enter contact name to update : ") 
        if name in contacts:
            age = input("Enter updated age : ")
            email = input("Enter updated email : ")
            mobile = input("Enter updated mobile number : ") 
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
        else:
            print("Contact not found")

    # Delete a contact
    elif choice == '4':
        name = input("Enter name to delete : ")
        if name in contacts:
            del contacts[name]
            print(f'Contact name {name} has been deleted successfully ')
        else:
            print('Contact not found')

    # Search for a contact by name (partial match allowed)
    elif choice == '5':
        search_name = input('Enter contact name to search: ')
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                # Display contact details when found
                print(f'Found\nName: {name}\nAge: {contact["age"]}\nMobile number: {contact["mobile"]}\nEmail: {contact["email"]}')
                found = True
        if not found:
            print('No contact found with that name')

    # Show the total number of contacts
    elif choice == '6':
        print(f'Total contacts in your book is : {len(contacts)}')

    # Exit the program
    elif choice == '7':
        print('Goodbye! Closing the program.')
        break

    # Handle invalid menu choices
    else:
        print("Invalid choice. Please select a valid option.")
