import json
import re


class Contacts:
    def __init__(self):
        self.contacts = self.load_contacts_from_file()

    def add_contact(self):
        contact_id = self.get_unique_id()
        name = self.get_valid_name()
        email = self.get_valid_email()
        phone = self.get_valid_phone()

        contact = {
            "id": contact_id,
            "name": name,
            "email": email,
            "phone": phone
        }
        self.contacts.append(contact)
        self.save_contacts_to_file()
        print("Contact added successfully.")

    def edit_contact(self):
        contact_id = input("Enter contact ID to edit: ")
        for contact in self.contacts:
            if contact["id"] == contact_id:
                name = input("Enter new contact name (leave empty to keep the old name): ")
                email = input("Enter new contact email (leave empty to keep the old email): ")
                phone = input("Enter new contact phone (leave empty to keep the old phone): ")

                if name:
                    name = self.get_valid_name(name)
                    contact["name"] = name
                if email:
                    email = self.get_valid_email(email)
                    contact["email"] = email
                if phone:
                    phone = self.get_valid_phone(phone)
                    contact["phone"] = phone

                self.save_contacts_to_file()
                print("Contact edited successfully.")
                return
        print("Contact not found.")

    def delete_contact(self):
        contact_id = input("Enter contact ID to delete: ")
        for contact in self.contacts:
            if contact["id"] == contact_id:
                self.contacts.remove(contact)
                self.save_contacts_to_file()
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

    def search_contact_by_id(self):
        contact_id = input("Enter contact ID to search: ")
        for contact in self.contacts:
            if contact["id"] == contact_id:
                print("Contact found:")
                print("ID: ", contact["id"])
                print("Name: ", contact["name"])
                print("Email: ", contact["email"])
                print("Phone: ", contact["phone"])
                return
        print("Contact not found.")

    def show_all_contacts(self):
        if len(self.contacts) == 0:
            print("No contacts found.")
            return

        print("Contacts:")
        print("{:<5} {:<20} {:<30} {:<15}".format("ID", "Name", "Email", "Phone"))
        for contact in self.contacts:
            print("{:<5} {:<20} {:<30} {:<15}".format(
                contact["id"], contact["name"], contact["email"], contact["phone"]
            ))

    def load_contacts_from_file(self):
        try:
            with open("contacts.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_contacts_to_file(self):
        with open("contacts.json", "w") as file:
            json.dump(self.contacts, file)

    def get_unique_id(self):
        while True:
            contact_id = input("Enter contact ID: ")
            if not any(contact["id"] == contact_id for contact in self.contacts):
                return contact_id
            print("ID already exists. Please enter a unique ID.")

    def get_valid_name(self, name=None):
        while True:
            if not name:
                name = input("Enter contact name: ")
            if name.isalpha():
                return name
            name = None
            print("Invalid name. Please enter a valid name.")

    def get_valid_email(self, email=None):
        while True:
            if not email:
                email = input("Enter contact email: ")
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                return email
            email = None
            print("Invalid email. Please enter a valid email.")

    def get_valid_phone(self, phone=None):
        while True:
            if not phone:
                phone = input("Enter contact phone: ")
            if phone.isdigit():
                return phone
            phone = None
            print("Invalid phone number. Please enter a valid phone number.")


def print_menu():
    print("Menu:")
    print("1. Add contact")
    print("2. Edit contact")
    print("3. Delete contact")
    print("4. Search contact by ID")
    print("5. Show all contacts")
    print("0. Exit")


contacts = Contacts()

while True:
    print_menu()
    choice = input("Enter your choice: ")

    if choice == "0":
        break
    elif choice == "1":
        contacts.add_contact()
    elif choice == "2":
        contacts.edit_contact()
    elif choice == "3":
        contacts.delete_contact()
    elif choice == "4":
        contacts.search_contact_by_id()
    elif choice == "5":
        contacts.show_all_contacts()
    else:
        print("Invalid choice. Please try again.")
