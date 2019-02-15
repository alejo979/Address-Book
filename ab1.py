# Create your own command-line address-book program using which you can browse, add, modify, delete or search for your contacts
# such as friends, family and colleagues and their information such as email address and/or phone number.
# Details must be stored for later retrieval.

import pickle
from pathlib import Path

abfile = 'abfile.pkl'                                               # where data is stored

if not Path('abfile.pkl').exists():               # Si no existe  # C:\\Py\\Projects\\
    ab = {}                                                         # Create empty Dictionary
else:
    f = open("abfile.pkl","rb")
    ab = pickle.load(f)

print('''Welcome to your address book  (Current Contacts: {})'''.format(len(ab)))

def print_main_menu():
    print('''What do you want to do?  
            1: Create a contact
            2: Find a contact
            3: Show all your contacts
            4: Update a contact
            5: Delete a contact
            6: Exit''')

def input_selection_func():
    global input_Selection
    input_Selection = int(input('Type a number >>> '))

def next_step_func():
    next_step = int(input('\nDo you want to (0)Exit or go back to (1)Main menu?>>> '))
    while True:
        if next_step == 0:
            global running
            running = False
            break
        else:
            print_main_menu()
            break


class Contact:
        def __init__(self,name,email,tel):
            self.name = name
            self.email = email
            self.tel = tel
        def whoIam(self):
            print('Contact created >>>',
                  'Name:',self.name,
                  '   E-mail:',self.email,
                  '   Tel:',self.tel)


print_main_menu()
running = True
while running:
    input_Selection = int(input('Type a number >>> '))

    if input_Selection == 1:                                                # Create a contact
        print('Creating contact:')
        contact1_name = input('Type the name: ')
        contact1_email = input('Type in the email: ')
        contact1_tel = input('Type in Tel: ')
        contact1 = Contact(contact1_name,contact1_email,contact1_tel)
        contact1.whoIam()

        ab[contact1_name] = [contact1_email, contact1_tel]

        print('You have now {} contacts'.format(len(ab)))

        f = open(abfile, 'wb')
        pickle.dump(ab, f)
        f.close()
        next_step_func()

    elif input_Selection == 2:                                              # Find a contact by name
        print('Finding contact:')
        find2 = input('Type in the name: ')
        if find2 in ab:
            for key,value in ab.items():
                if key == find2:
                    print(value)
                    next_step_func()

        else:
            print('Contact does not exist')
            next_step_func()

    elif input_Selection == 3:                                              # Show all contacts
        print("All your contacts and details:")
        #print(sorted(ab))   --- this just prints the keys
        for key,value in sorted(ab.items(), key=lambda x: x[0]):
            print(key,value, sep='\t')    # for snack in fruit: print(fruit[snack]) >> just prints the values, not the keys
        next_step_func()

    elif input_Selection == 4:                                              # Update a contact by name
        update4 = input("Type in the contact's name to update: ")
        if update4 in ab:
            running4 = True
            while running4:
                    print('''What do you want to update:
                    (1: Email
                    2: Tel)''')
                    update4_selection = int(input('>>> '))
                    if update4_selection == 1:
                        print('Current email: {}'.format(ab[update4][0]))
                        update4_1 = input('Type the new email: ')
                        ab[update4][0] = update4_1
                        print('New email is: {}'.format(ab[update4][0]))
                        f = open(abfile, 'wb')
                        pickle.dump(ab, f)
                        f.close()
                        next_step_func()
                        running4 = False
                    elif update4_selection == 2:
                        print('Current Tel: {}'.format(ab[update4][1]))
                        update4_2 = input('Type the new Tel: ')
                        ab[update4][1] = update4_2
                        print('New Tel is: {}'.format(ab[update4][1]))
                        f = open(abfile, 'wb')
                        pickle.dump(ab, f)
                        f.close()
                        next_step_func()
                        running4 = False
                    else:
                        print('Please choose 1 or 2')
            #else:
                #print('Done loop inside 1email or 2tel')
        else:
            print('Contact does not exist')
            next_step_func()

    elif input_Selection == 5:                                              # Delete a contact by name
        delete4 = input("Type in the contact's name to delete: ")
        del ab[delete4]
        print('Contact {} has been deleted'.format(delete4))
        f = open(abfile, 'wb')
        pickle.dump(ab, f)
        f.close()
        next_step_func()

    elif input_Selection == 6:                                              # Exit
        break

print('Goodbye and come back soon')
