from AddressBook import *


class Bot:
    def __init__(self):
        self.book = AddressBook()

    def handle(self, action):
        if action == "add":
            self.add_contact()
        elif action == "search":
            self.search_contacts()
        elif action == "edit":
            self.edit_contact()
        elif action == "remove":
            self.remove_contact()
        elif action == "save":
            self.save_to_file()
        elif action == "load":
            self.load_from_file()
        elif action == "congratulate":
            self.congratulate()
        elif action == "view":
            self.view_contacts()
        elif action == "exit":
            pass
        else:
            print("No such command!")

    def add_contact(self):
        name = Name(input("Name: ")).value.strip()
        phones = Phone().value
        birth = Birthday().value
        email = Email().value.strip()
        status = Status().value.strip()
        note = Note(input("Note: ")).value
        record = Record(name, phones, birth, email, status, note)
        self.book.add(record)

    def search_contacts(self):
        print(
            "Available categories for search: \nName \nPhones \nBirthday \nEmail \nStatus \nNote"
        )
        category = input("Choose a category for search: ")
        pattern = input("Enter a search pattern: ")
        result = self.book.search(pattern, category)
        for account in result:
            if account["birthday"]:
                birth = account["birthday"].strftime("%d/%m/%Y")
                result = (
                    "_" * 50
                    + "\n"
                    + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n"
                    + "_" * 50
                )
                print(result)

    def edit_contact(self):
        contact_name = input("Contact name: ")
        parameter = input(
            "Which parameter do you want to change (name, phones, birthday, status, email, note): "
        ).strip()
        new_value = input("New value: ")
        self.book.edit(contact_name, parameter, new_value)

    def remove_contact(self):
        pattern = input("Delete (contact name or phone number): ")
        self.book.remove(pattern)

    def save_to_file(self):
        file_name = input("File name: ")
        self.book.save(file_name)

    def load_from_file(self):
        file_name = input("File name: ")
        self.book.load(file_name)

    def congratulate(self):
        print(self.book.congratulate())

    def view_contacts(self):
        print(self.book)


class UserInterface:
    def __init(self):
        self.bot = Bot()

    def run(self):
        while True:
            action = input("Enter a command: ")
            self.bot.handle(action)
            if action == "exit":
                break


if __name__ == "__main__":
    interface = UserInterface()
    interface.run()
