def add_contact(contact_list):
    name = input("Name: ")
    phone = input("Phone: ")
    contact_list.append(name + " - " + phone)
    print("Added!")
def show_contacts(contact_list):
    if len(contact_list) == 0:
        print("No contacts yet")
    else:
        for i in range(len(contact_list)):
            print(i + 1, ":", contact_list[i])
def search_contact(contact_list):
    name = input("Search name: ")
    found = False
    for c in contact_list:
        if name in c:
            print(c)
            found = True
    if found == False:
        print("Not found")
def main():
    my_contacts = []
    while True:
        print("1. Add, 2. Display, 3. Search, 4. Exit")
        choice = input("Select: ")

        if choice == '1':
            add_contact(my_contacts)
        elif choice == '2':
            show_contacts(my_contacts)
        elif choice == '3':
            search_contact(my_contacts)
        elif choice == '4':
            break
main()
