import stdiomask
from time import sleep

def login_menu():
    print("""\n           Login Page
======================================
        """)

    username = input("Username: ").strip()[:15]
    password = stdiomask.getpass(prompt='Password: ', mask='*')

    login(username, password)

def login(username, password):
    if (search_user(username, password)):
        print("\nYou are now logged in {}!!!\n".format(username))
        sleep(1.2)
        while True:
            print("""\n            Dashboard
======================================
1. See All Users
2. Change Your Username
3. Change Your Password
4. Delete Your User
5. Log Out (Exit)
======================================
        """)

            try:
                option = int(input("Enter an option: "))

                if option == 1:
                    all_users()
                    continue
                elif option == 2:
                    change_user(username=username)
                    print("Username Successfully Updated!")
                    sleep(2)
                    break
                elif option == 3:
                    change_user(username=username, password=password)
                    print("Password Successfully Updated!")
                    sleep(2)
                    break
                elif option == 4:
                    change_user(username=username, delete=True)
                    print("User Successfully Deleted!")
                    sleep(2)
                    break
                elif option == 5:
                    print("\nLogging Out...")
                    sleep(1.5)
                    break
                else:
                    print("\nInvalid Option! Try Again...\n")
                    sleep(1)
                    continue
            except ValueError:
                print("\nPlease, enter a valid numeric number.\n")
                sleep(1)
                continue
            except KeyboardInterrupt:
                print("\nYou have choosen to leave.")
                sleep(1)
                break
            finally:
                print("======================================")
    else:
        print("No User with those credentials found!")
        sleep(1.2)

def search_user(username, password):
    try:
        with open('/home/gustavos/Python3/SCRU/data.txt', 'r+') as file:
            for raw_line in file:
                line = raw_line.strip().split(',')

                temp_username, temp_password = line[0], line[1]

                if (temp_username == username and temp_password == password):
                    return True

            return False

    except:
        print("An error was found. Either path is incorrect or file doesn't exist!")

                
def change_user(username=None, password=None, delete=False):
    with open("/home/gustavos/Python3/SCRU/data.txt", "r") as f:
        lines = f.readlines()
    with open("/home/gustavos/Python3/SCRU/data.txt", "w") as f:
        for line in lines:
            if delete:
                if line.strip("\n").split(",")[0] != username:
                    f.write(line)
            elif password and username:
                if line.strip("\n").split(",")[0] != username:
                    f.write(line)
                else:
                    new_password = stdiomask.getpass(prompt='New password: ', mask='*')
                    f.write("{},{}\n".format(username, new_password))
            else:
                if line.strip("\n").split(",")[0] != username:
                    f.write(line)
                else:
                    new_username = input("New username: ").strip()[:15]
                    f.write("{},{}\n".format(new_username, line.strip().split(",")[1]))

def all_users():
    try:
        with open('/home/gustavos/Python3/SCRU/data.txt', 'r+') as file:
            i = 1
            for line in file:
                print("[{}] Username: {}".format(i, line.strip().split(",")[0]))
                i += 1
            sleep(2)
    except:
        print("Problems opening some file")