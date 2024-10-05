# # This is a Python code example demonstrating how to implement a basic laundry slot booking system.
# # This code is based on the information provided in the image. It's a simplified representation and
# # may need to be adapted based on your specific requirements.

# class SlotBookingSystem:
#     def _init_(self, num_rooms=3, slots_per_room=5, days_in_cycle=12):
#         self.num_rooms = num_rooms
#         self.slots_per_room = slots_per_room
#         self.days_in_cycle = days_in_cycle
#         self.room_slots = {}
#         self.student_slots = {}
#         self.reset_slots()

#     def reset_slots(self):
#         # Initialize slots for each room
#         for room_num in range(1, self.num_rooms + 1):
#             self.room_slots[room_num] = [True] * self.slots_per_room

#         # Initialize slots for each student (empty)
#         self.student_slots = {}

#     def display_room_summary(self):
#         print("Room Slot Summary:")
#         for room_num in range(1, self.num_rooms + 1):
#             available_slots = self.room_slots[room_num].count(True)
#             print(f"Room {room_num}: {available_slots} / {self.slots_per_room} slots available")

#     def display_student_slots(self, student_id):
#         if student_id in self.student_slots:
#             print(f"Student {student_id} booked slots:")
#             for day in range(self.days_in_cycle):
#                 if self.student_slots[student_id][day] is not None:
#                     print(f"Day {day + 1}: Room {self.student_slots[student_id][day]}")
#         else:
#             print(f"Student {student_id} has not booked any slots.")

#     def book_slot(self, student_id, day, room_num):
#         if day < 0 or day >= self.days_in_cycle:
#             print("Invalid day. Day must be between 1 and", self.days_in_cycle)
#             return False

#         if room_num not in self.room_slots:
#             print("Invalid room number.")
#             return False

#         if self.room_slots[room_num][day]:
#             # Check if the student has already booked for that day
#             if student_id in self.student_slots and self.student_slots[student_id][day] is not None:
#                 print("You have already booked a slot for this day.")
#                 return False

#             # Book the slot
#             self.room_slots[room_num][day] = False
#             if student_id not in self.student_slots:
#                 self.student_slots[student_id] = [None] * self.days_in_cycle
#             self.student_slots[student_id][day] = room_num
#             print(f"Slot booked successfully for Room {room_num} on Day {day + 1}.")
#             return True
#         else:
#             print("Slot is already booked for this day.")
#             return False

#     def enforce_slot_limit(self, student_id, day):
#         # Check if the student has booked more than one slot for the day
#         if student_id in self.student_slots and self.student_slots[student_id][day] is not None:
#             print("You cannot book more than one slot per day.")
#             return False
#         return True

#     def check_overbooking(self, day):
#         # Check if the maximum number of slots is booked for the day
#         total_booked = 0
#         for room_num in self.room_slots:
#             if not self.room_slots[room_num][day]:
#                 total_booked += 1

#         max_allowed = self.num_rooms * self.slots_per_room
#         if total_booked == max_allowed:
#             print("All slots are booked for this day.")
#             return True
#         return False

#     def run(self):
#         while True:
#             print("\nLaundry Slot Booking System")
#             print("1. Display Room Summary")
#             print("2. Display Student Slots")
#             print("3. Book Slot")
#             print("4. Exit")

#             choice = input("Enter your choice: ")

#             if choice == '1':
#                 self.display_room_summary()
#             elif choice == '2':
#                 student_id = int(input("Enter student ID: "))
#                 self.display_student_slots(student_id)
#             elif choice == '3':
#                 student_id = int(input("Enter student ID: "))
#                 day = int(input("Enter day (1 - {}): ".format(self.days_in_cycle))) - 1
#                 room_num = int(input("Enter room number: "))
#                 if self.enforce_slot_limit(student_id, day) and not self.check_overbooking(day):
#                     self.book_slot(student_id, day, room_num)
#             elif choice == '4':
#                 break
#             else:
#                 print("Invalid choice.")

# # Example usage
# system = SlotBookingSystem()
# system.run()


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"
class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully✅.")

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact {name} removed ❌ successfully.")
                return
        print(f"Contact {name} not found.")

    def update_contact(self, name, phone=None, email=None):
        for contact in self.contacts:
            if contact.name == name:
                if phone:
                    contact.phone = phone
                if email:
                    contact.email = email
                print(f"Contact {name} updated successfully.")
                return
        print(f"Contact {name} not found.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(contact)
                return
        print(f"Contact {name} not found.")

    def list_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        for contact in self.contacts:
            print(contact)
def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Update Contact")
        print("4. Search Contact")
        print("5. List Contacts")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact = Contact(name, phone, email)
            contact_book.add_contact(contact)
        
        elif choice == '2':
            name = input("Enter name of the contact to remove: ")
            contact_book.remove_contact(name)
        
        elif choice == '3':
            name = input("Enter name of the contact to update: ")
            phone = input("Enter new phone (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            contact_book.update_contact(name, phone if phone else None, email if email else None)
        
        elif choice == '4':
            name = input("Enter name of the contact to search: ")
            contact_book.search_contact(name)
        
        elif choice == '5':
            contact_book.list_contacts()
        
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
