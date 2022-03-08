import createProjects
import ViewProjects
import EditingMenu
import DeleteProject
import Searching


def loginMenu(userEmail):
    while True:
        print("*************************************************************************")
        print("         Please, Enter Your choice carefully as You asked for            ")
        print("*************************************************************************")
        print("                     [1] Create a project                                ")
        print("                     [2] View all projects                               ")
        print("                     [3] Edit Your own Projects                          ")
        print("                     [4] Delete Your own project                         ")
        print("                     [5] Search for a project                            ")
        print("                     [6] Back                                            ")
        print("                     [00] Exit                                           ")
        print("*************************************************************************")
        print("")
        logginUserMail = userEmail
        choise = input("Your choise is : ")
        print("")
        if choise.isnumeric():
            choise = int(choise)
            if choise == 1:
                createProjects.createProject(logginUserMail)
            elif choise == 2:
                ViewProjects.viewProjects(logginUserMail)
            elif choise == 3:
                EditingMenu.editingRecord(logginUserMail)
            elif choise == 4:
                title = EditingMenu.checkingtitleValidation()
                DeleteProject.deleteRecord(logginUserMail, title)
            elif choise == 5:
                title = EditingMenu.checkingtitleValidation()
                Searching.recordSearching(logginUserMail, title)
            elif choise == 6:
                return
            elif choise == 00:
                print("Exit.....................!")
                exit()
            else:
                print("Invalid Choise, Try again")
        else:
            print("Invalid input")


# loginMenu("mohamed1@gmail.com")