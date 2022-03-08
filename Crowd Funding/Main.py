import registeration
import Login


print("***********************************************************")
print("*                                                         *")
print("*           Crowd-Funding Console Application             *")
print("*                                                         *")
print("***********************************************************")
print("")


def mainFun():
    while True:
        print("***********************************************************")
        print("*        Please, Carefully Choise from List blow:         *")
        print("*                  [1] Registration                       *")
        print("*                  [2] Login                              *")
        print("*                  [3] Exit                               *")
        print("***********************************************************")
        print("")
        Choise = input("Enter Your choise: ").strip()
        if Choise.isnumeric():
            Choise = int(Choise)
            if Choise == 1:
                print("You Now in Registeration mode..........!")
                print("")
                registeration.registerationForm()
            elif Choise == 2:
                print("You Now in Login mode..........!")
                print("")
                Login.login()
            elif Choise == 3:
                print("Exit............!")
                exit()
            else:
                print("Invalid Input")

        else:
            print("You Enter invalid Input")


mainFun()
