import EditingTitle
import EditingDiscription
import EditingTotalTarget
import EdittingStartDate
import EdittingEndDate


def checkingtitleValidation():
    while True:
        checkTitle = input("Please Enter the Title of project: ").strip()
        if checkTitle.isalnum():
            checkTitle = str(checkTitle)
            return checkTitle
        else:
            print("Invalid Type of title")
            checkingtitleValidation()


def editingRecord(userEmail):
    while True:
        print("*************************************************************************")
        print("           Please, Enter Your choice carefully as You asked for          ")
        print("*************************************************************************")
        print("                           [1] Edit Title                                ")
        print("                           [2] Edit Description                          ")
        print("                           [3] Edit Total Target                         ")
        print("                           [4] Edit Start Date                           ")
        print("                           [5] Edit End Date                             ")
        print("                           [00] Back                                     ")
        print("*************************************************************************")
        print("")
        email = userEmail
        choise = input("Your choise is : ")
        print("")
        if choise.isnumeric():
            choise = int(choise)
            if choise == 1:
                checkTitle = checkingtitleValidation()
                EditingTitle.editingTitle(email, checkTitle)
            elif choise == 2:
                checkTitle = checkingtitleValidation()
                EditingDiscription.editingDescription(email, checkTitle)
            elif choise == 3:
                checkTitle = checkingtitleValidation()
                EditingTotalTarget.editingTotalTarget(email, checkTitle)
            elif choise == 4:
                checkTitle = checkingtitleValidation()
                EdittingStartDate.editStartDate(email, checkTitle)
            elif choise == 5:
                checkTitle = checkingtitleValidation()
                EdittingEndDate.editEndDate(email, checkTitle)
            elif choise == 00:
                return
            else:
                print("Invalid Choise, Try again")
        else:
            print("Invalid Input")
    return



# editingRecord("mohamed@gmail.com")
