import inserting
import Checking
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def nameValidation(varname):
    att = input(f"Enter your {varname} : ").strip()
    if att.isalpha():
        return att
    else:
        return nameValidation(varname)


def emailValidation(Email):
    Email = input("Enter Your Mail : ").strip()
    if re.fullmatch(regex, Email):
        if Checking.checkEmail(Email):
            return Email
        else:
            return emailValidation(Email)
    else:
        print("Invalid Email type,Please try again...!")
        return emailValidation(Email)


def passValidation(password):
    Password = input(f"Enter your Password : ").strip()

    SpecialSym = ['$', '@', '#', '_', '-', '!', '%', '&']
    val = True

    if len(Password) < 6:
        print('length should be at least 6')
        val = False

    if len(Password) > 20:
        print('length should be not be greater than 8')
        val = False

    if not any(char.isdigit() for char in Password):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in Password):
        print('Password should have at least one uppercase letter')
        val = False
    if not any(char.islower() for char in Password):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialSym for char in Password):
        print('Password should have at least one of the symbols [$@#_-!%&]')
        val = False
    if val:
        return Password
    else:
        return passValidation(Password)


def conPassValidation(password):
    cofPassword = input("Confirm Your Password : ")

    if password == cofPassword:
        return cofPassword
    else:
        print("Not Matched Password,please try again")
        return conPassValidation(password)


def phoneNumValidation(phoneNum):
    number = input("Please Enter Your Phone Number: ")
    if len(number) < 11 or len(number) > 11:
        print("Please Enter a valid Phone number")
        return phoneNumValidation(phoneNum)
    else:
        if number.startswith('010') or number.startswith('011') or number.startswith('012') or number.startswith('015'):
            return number
        else:
            print("invalid Number in Egypt, please Enter a valid Number")
            return phoneNumValidation(phoneNum)


def registerationForm():
    fname = nameValidation("fname")
    lname = nameValidation("lname")
    Email = emailValidation("Email")
    password = passValidation("password")
    conPassword = conPassValidation(password)
    phoneNum = phoneNumValidation("phoneNum")
    userInfo = [fname, lname, Email, password, conPassword,phoneNum]
    inserting.insert(userInfo)
    return
