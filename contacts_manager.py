# Name: Saniya Choughule
# Week 3 Project
# Contact Management System

# Import required modules
import json
import csv
import re
import os

# Dictionary to store contacts
contacts = {}

# -------------------------------
# Validate Phone Number
# -------------------------------
def validate_phone(phone):

    # Remove spaces from phone number
    phone = phone.replace(" ", "")

    # Check if phone contains only digits and has 10 digits
    if phone.isdigit() and len(phone) == 10:
        return True
    else:
        return False


# -------------------------------
# Validate Email
# -------------------------------
def validate_email(email):

    # Email is optional
    if email == "":
        return True

    # Basic email pattern
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(pattern, email):
        return True
    else:
        return False


# -------------------------------
# Load Contacts from JSON File
# -------------------------------
def load_contacts():

    global contacts

    if os.path.exists("contacts_data.json"):

        with open("contacts_data.json", "r") as file:

            try:
                contacts = json.load(file)
                print("\nContacts loaded successfully.")

            except json.JSONDecodeError:
                contacts = {}

    else:
        contacts = {}


# -------------------------------
# Save Contacts to JSON File
# -------------------------------
def save_contacts():

    with open("contacts_data.json", "w") as file:

        json.dump(contacts, file, indent=4)

    print("\nContacts saved successfully.")


# -------------------------------
# Add New Contact
# -------------------------------
def add_contact():

    print("\nADD NEW CONTACT")

    # Get Name
    while True:

        name = input("Enter Name: ").title().strip()

        if name == "":
            print("Name cannot be empty.")
            continue

        if name in contacts:
            print("Contact already exists.")
            return

        break

    # Get Phone Number
    while True:

        phone = input("Enter Phone Number: ")

        if validate_phone(phone):
            break

        print("Invalid phone number. Enter exactly 10 digits.")

    # Get Email
    while True:

        email = input("Enter Email (optional): ").lower().strip()

        if validate_email(email):
            break

        print("Invalid Email.")

    # Get Address
    address = input("Enter Address: ").title().strip()

    # Get Group
    group = input("Enter Group (Friends/Family/Work): ").title().strip()

    if group == "":
        group = "Other"

    # Store Contact
    contacts[name] = {

        "phone": phone,
        "email": email,
        "address": address,
        "group": group

    }

    save_contacts()

    print("Contact Added Successfully.")


# -------------------------------
# Search Contact
# -------------------------------
def search_contact():

    search = input("\nEnter Name to Search: ").lower().strip()

    found = False

    print("\nSEARCH RESULTS")
    print("-" * 40)

    for name, details in contacts.items():

        if search in name.lower():

            print(f"\nName    : {name}")
            print(f"Phone   : {details['phone']}")
            print(f"Email   : {details['email']}")
            print(f"Address : {details['address']}")
            print(f"Group   : {details['group']}")

            found = True

    if not found:
        print("No Contact Found.")


# -------------------------------
# Display Search Results
# -------------------------------
def display_contacts():

    if len(contacts) == 0:

        print("\nNo Contacts Available.")
        return

    print("\nALL CONTACTS")
    print("=" * 50)

    for name, details in contacts.items():

        print(f"\nName    : {name}")
        print(f"Phone   : {details['phone']}")
        print(f"Email   : {details['email']}")
        print(f"Address : {details['address']}")
        print(f"Group   : {details['group']}")

        print("-" * 50)

# -------------------------------
# Update Contact
# -------------------------------
def update_contact():

    name = input("\nEnter Contact Name to Update: ").title().strip()

    if name not in contacts:
        print("Contact not found.")
        return

    print("\nLeave blank if you don't want to change a value.")

    # Update Phone Number
    phone = input("New Phone Number: ").strip()

    if phone != "":
        while not validate_phone(phone):
            print("Invalid phone number.")
            phone = input("New Phone Number: ").strip()

        contacts[name]["phone"] = phone

    # Update Email
    email = input("New Email: ").lower().strip()

    if email != "":
        while not validate_email(email):
            print("Invalid email.")
            email = input("New Email: ").lower().strip()

        contacts[name]["email"] = email

    # Update Address
    address = input("New Address: ").title().strip()

    if address != "":
        contacts[name]["address"] = address

    # Update Group
    group = input("New Group: ").title().strip()

    if group != "":
        contacts[name]["group"] = group

    save_contacts()

    print("Contact Updated Successfully.")


# -------------------------------
# Delete Contact
# -------------------------------
def delete_contact():

    name = input("\nEnter Contact Name to Delete: ").title().strip()

    if name not in contacts:
        print("Contact not found.")
        return

    confirm = input(f"Delete {name}? (Y/N): ").upper()

    if confirm == "Y":
        del contacts[name]
        save_contacts()
        print("Contact Deleted Successfully.")

    else:
        print("Delete Cancelled.")


# -------------------------------
# Export Contacts to CSV
# -------------------------------
def export_csv():

    with open("contacts.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Name", "Phone", "Email", "Address", "Group"])

        for name, details in contacts.items():

            writer.writerow([
                name,
                details["phone"],
                details["email"],
                details["address"],
                details["group"]
            ])

    print("Contacts exported to contacts.csv")


# -------------------------------
# Contact Statistics
# -------------------------------
def statistics():

    print("\nCONTACT STATISTICS")
    print("-" * 30)

    total = len(contacts)

    friends = 0
    family = 0
    work = 0
    other = 0

    for details in contacts.values():

        group = details["group"].lower()

        if group == "friends":
            friends += 1

        elif group == "family":
            family += 1

        elif group == "work":
            work += 1

        else:
            other += 1

    print("Total Contacts :", total)
    print("Friends        :", friends)
    print("Family         :", family)
    print("Work           :", work)
    print("Other          :", other)


# -------------------------------
# Main Menu
# -------------------------------
def menu():

    print("\n" + "=" * 45)
    print("CONTACT MANAGEMENT SYSTEM")
    print("=" * 45)

    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Export to CSV")
    print("7. Statistics")
    print("8. Exit")


# -------------------------------
# Main Function
# -------------------------------
def main():

    load_contacts()

    while True:

        menu()

        choice = input("\nEnter Your Choice (1-8): ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            search_contact()

        elif choice == "3":
            update_contact()

        elif choice == "4":
            delete_contact()

        elif choice == "5":
            display_contacts()

        elif choice == "6":
            export_csv()

        elif choice == "7":
            statistics()

        elif choice == "8":

            save_contacts()

            print("\nThank You for using Contact Management System.")
            break

        else:
            print("Invalid Choice. Please try again.")


# -------------------------------
# Program Starts Here
# -------------------------------
if __name__ == "__main__":
    main()