import Checking
import LoginMenu


def login():
    Email = input("Enter Your Email:").strip()
    Password = input("Enter Your Password:").strip()
    if Checking.checklogin(Email, Password):
        print("*************************************************************************")
        print("                         Loging Successfully....!                        ")
        print("*************************************************************************")
        LoginMenu.loginMenu(Email)
        return True
    print("Invalid username or Email ,Please Try again")
    return login()


# login()
# 01064025379