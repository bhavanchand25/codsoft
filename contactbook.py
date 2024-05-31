class Contact:
    def __init__(self, name, phone, email="", address=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def search_contact(self, query):
        query = query.lower()
        results = []
        for contact in self.contacts:
            if query in contact.name.lower() or query in contact.phone:
                results.append(contact)
        return results

    def delete_contact(self, contact):
        self.contacts.remove(contact)

    def view_all_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

def main():
    my_contact_book = ContactBook()

    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email (optional): ")
            address = input("Enter address (optional): ")
            contact = Contact(name, phone, email, address)
            my_contact_book.add_contact(contact)
            print("Contact added successfully!")

        elif choice == "2":
            query = input("Enter name or phone number to search: ")
            results = my_contact_book.search_contact(query)
            if results:
                print("Search results:")
                for result in results:
                    print(f"Name: {result.name}, Phone: {result.phone}")
            else:
                print("No matching contacts found.")

        elif choice == "3":
            query = input("Enter name or phone number to delete: ")
            results = my_contact_book.search_contact(query)
            if results:
                for result in results:
                    my_contact_book.delete_contact(result)
                print("Contact(s) deleted successfully!")
            else:
                print("No matching contacts found.")

        elif choice == "4":
            my_contact_book.view_all_contacts()

        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break

if __name__ == "__main__":
    main()
