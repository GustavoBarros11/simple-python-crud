from os import system
from time import sleep
import signup_page as signup
import login_page as login

def main():
    while True:
        print("""\n            Main Menu
======================================
1. Login
2. Sign-up
3. Exit
======================================
        """)

        try:
            option = int(input("Enter an option: "))

            if option == 1:
                login.login_menu()
                continue
            elif option == 2:
                signup.signup_menu()
                continue
            elif option == 3:
                print("\nExiting...")
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
        

if __name__ == '__main__':
    main()