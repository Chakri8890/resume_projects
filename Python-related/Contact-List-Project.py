class Details():
    def __init__(self,Name,EMail,Phone):
        self.Name = Name
        self.EMail = EMail
        self.Phone = Phone

    def display(self):
        print(f'Name :{self.Name} , EMail:{self.EMail} , Phone:{self.Phone}')

    def __str__(self):
        print(f'Name:{self.Name}, Email:{self.EMail}, Phone:{self.Phone}')

class ContactBook():
    def __init__(self):
        self.contacts = []

    def AddContact(self,contact):
        self.contacts.append(contact)
        print(f'Contact "{contact.Name}" is Added Successfully✅')

    def RemoveContact(self,name):
        for contact in self.contacts:
            if contact.Name == name:
                self.contacts.remove(contact)
                print(f'Contact {name} removed ❌ successfully..')
                return
        print(f'Contact {name} is not Found!....')

    def UpdateContact(self,name,phone=None,Email=None):
        for contact in self.contacts:
            if contact.Name == name: 
                if phone:
                    contact.Phone == phone
                if Email:
                    contact.EMail == Email
                print(f'Contact {name} is Successfully Updated')
                return
        print(f'Contact {name} is Not Found')

    def SearchContact(self,name):
        for contact in self.contacts:
            if contact.Name == name:
                print(f'Contacts are :{name}')
                return
        print(f'Contact {name} Not Found!..')

    def DisplayAllContact(self):
        if not self.contacts:
            print("No Contact Found!...")
        for contact in self.contacts:
            print(f'Your Contacts are : {contact}')
            
def Main():
    contact_list = ContactBook()
    while True:
        print('\n CONTACT DETAILS')
        print('1.ADD CONTACT')
        print('2.REMOVE CONTACT')
        print('3.UPDATE CONTACT')
        print('4.SEARCH CONTACT')
        print('5.DISPLAY ALL CONTACTS')
        print('6.EXIT')

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            Name = input("Enter name:")
            EMail = input("Enter E-Mail")
            Phone = input("Enter PhoneNumber:")
            contact = Details(Name,EMail,Phone)
            contact_list.AddContact(contact)
        elif choice == 2:
            contact_list.RemoveContact(name)
        elif choice == 3:
            name = input("Enter your New Name to update:")
            phone = input("Enter your New phone.No to Update (Press Enter to Skip):")
            Email = input("Enter your New Email to update (Press Enter to Skip):")
            contact_list.UpdateContact(name , phone if phone else None,Email if Email else None)
        elif choice == 4:
            name = input("Enter your name to search Contact")
            contact_list.SearchContact(name)
        elif choice == 5:
            contact_list.DisplayAllContact()
        elif choice == 6:
            print("Exiting............")
            break
        else:
            print("Invalid !..Please Try again....")

Main()