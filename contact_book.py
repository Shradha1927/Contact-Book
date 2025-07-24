import json
import os
from colorama import Fore, Style, init

#  Initialize colorama 
init(autoreset=True)

# where contacts live
CONTACTS_FILE = "contacts.json"

#  Pastel 
PASTEL_GREEN = Fore.LIGHTGREEN_EX
PASTEL_BLUE = Fore.LIGHTBLUE_EX
PASTEL_PINK = Fore.LIGHTMAGENTA_EX
PASTEL_CYAN = Fore.CYAN
ERROR = Fore.RED
GRAY = Fore.LIGHTBLACK_EX

#  Load contacts from the JSON 
def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "w") as f:
            json.dump([], f)
    with open(CONTACTS_FILE, "r") as file:
        return json.load(file)

# Save contacts 
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new 
def add_contact(contacts):
    name = input("👤 Name: ")
    phone = input("📞 Phone: ")
    email = input("📧 Email: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })
    print(PASTEL_GREEN + "✨ Contact added.")

# Find the person
def search_contact(contacts):
    query = input("🔍 Name or phone? Drop it: ").lower()
    results = [c for c in contacts if query in c["name"].lower() or query in c["phone"]]
    if results:
        print(PASTEL_CYAN + f"🔎 Found {len(results)} human(s):")
        for i, c in enumerate(results, 1):
            print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")
    else:
        print(ERROR + "🚫 Contact Don't exist.")

# Make updates 
def update_contact(contacts):
    search_contact(contacts)
    try:
        index = int(input("🛠️ Which number to update? ")) - 1
        if 0 <= index < len(contacts):
            name = input(f"New name ({contacts[index]['name']}): ") or contacts[index]['name']
            phone = input(f"New phone ({contacts[index]['phone']}): ") or contacts[index]['phone']
            email = input(f"New email ({contacts[index]['email']}): ") or contacts[index]['email']
            contacts[index] = {"name": name, "phone": phone, "email": email}
            print(PASTEL_GREEN + "🔄 Updated like your Spotify Wrapped.")
        else:
            print(ERROR + "🤡 That's not a real option, brother.")
    except ValueError:
        print(ERROR + "⚠️ We said number, not alphabet .")

# delete the contact 
def delete_contact(contacts):
    search_contact(contacts)
    try:
        index = int(input("🧨 Number to yeet from list: ")) - 1
        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            print(PASTEL_PINK + f"💅 {removed['name']} has been removed from existence.")
        else:
            print(ERROR + "🚫 Wrong number.")
    except ValueError:
        print(ERROR + "⚠️ That’s not even a number.")

# Show connections
def list_contacts(contacts):
    if not contacts:
        print(GRAY + "🫠  Add someone?")
        return
    print(PASTEL_BLUE + "\n📇 Your Carefully Collected Contacts:")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")

# Main hub 
def main():
    contacts = load_contacts()
    print(PASTEL_CYAN + "\n👾 Welcome to the ✨ Gen Z Contact Book ✨")

    while True:
        print("\n🌀 MENU")
        print("1️⃣  View Contacts")
        print("2️⃣  Add Someone")
        print("3️⃣  Stalk Search")
        print("4️⃣  Update Their Info")
        print("5️⃣  Ghost/Delete")
        print("6️⃣  Save & Exit 🫡")

        choice = input("💭 What now? ")

        if choice == "1":
            list_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print(GRAY + "📁 Saved. Catch you on the flip side 🛸")
            break
        else:
            print(ERROR + "🚫 Nope. That’s not valid.")

if __name__ == "__main__":
    main()
