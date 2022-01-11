import stdiomask as stdiomask
from time import sleep

def signup_menu():
    try:
        print("""\n          Sing-Up Page
======================================
        """)

        username = input("New username: ").strip()[:15]
        password = stdiomask.getpass(prompt='Password: ', mask='*')

        if len(username) < 3:
            print("Username needs to be at least 3 characters long.")
            sleep(2)
        elif len(password) < 4:
            print("Password needs to be at least 4 characters long.")
            sleep(2)
        else:
            is_already_user = search_user(username, password)

            if is_already_user:
                print("This emails is already been used! Try Again.")
                sleep(2)
            else:
                signup_logic(username, password)
    except KeyboardInterrupt:
        print("\nBack to Main Menu. Press Crl+c again to leave the program.")
        sleep(1)

def signup_logic(username, password):
    try:
        with open('/home/gustavos/Python3/SCRU/data.txt', 'a+') as file:
            file.write('{},{}\n'.format(username, password))
            print("Signed In Successfully. Please, now login.")
            sleep(2)
    except:
        print("Error")

def search_user(username, password):
    try:
        with open('/home/gustavos/Python3/SCRU/data.txt', 'r+') as file:
            for raw_line in file:
                temp_username = raw_line.split(',')[0]

                if (temp_username == username):
                    return True

            return False

    except:
        print("An error was found. Either path is incorrect or file doesn't exist!")

if __name__ == '__main__':
    signup_menu()