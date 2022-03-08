import Checking
import addnewProjects
import datetime


def titleValidation(title):
    projTitle = input("Enter your project Title : ").strip()
    if projTitle.isalpha():
        if Checking.checkTitle(projTitle):
            return projTitle
        else:
            return titleValidation(title)
    else:
        return titleValidation(title)


def totalTargetValidation(details):
    projDetails = input("Your Total target in dollars: ")
    if projDetails.isnumeric():
        projDetails = str(projDetails)
        return projDetails
    else:
        print("invalid input ")
        return totalTargetValidation(details)


def startDateValidation(date):
    startDate = input(f"Enter project {date} date: ")
    try:
        datetime.datetime.strptime(startDate, '%Y-%m-%d')
        return startDate
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")
        return startDateValidation(date)


def endDateValidation(start):
    endDate = input(f"Enter project End date: ")
    try:
        datetime.datetime.strptime(endDate, '%Y-%m-%d')
        if start < endDate:
            return endDate
        else:
            print("End date can not be before Start date")
            return endDateValidation(start)
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")
        return endDateValidation(start)


def createProject(userMail):
    userEmail = userMail
    title = titleValidation("title")
    details = input("Project Details: ")
    totalTarget = totalTargetValidation("totalTarget")
    Start = startDateValidation("Start")
    End = endDateValidation(Start)
    projInfo = [userEmail, title, details, totalTarget, Start, End]
    addnewProjects.addProject(projInfo)
    return
