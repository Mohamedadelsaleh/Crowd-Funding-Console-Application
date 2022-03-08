import os


def editingDescription(usermail, title):
    projectTitle = title
    email = usermail
    flag = 0
    # filWrite = open("Projects/temp.txt", "w")
    with open("Projects/projects.txt") as readFile:
        projects = readFile.readlines()
        for project in projects:
            project = project.strip("\n")
            project_info = project.split(":")
            if email == project_info[0]:
                if projectTitle == project_info[1]:
                    newDes = input("Enter Your New Description : ")
                    project_info[2] = newDes
                    finalInfor = ":".join(project_info)
                    with open("Projects/temp.txt", "a") as editingFile:
                        data = finalInfor.strip("\n")
                        data = f"{data}\n"
                        editingFile.writelines(data)
                        print("*************************************************************************")
                        print("")
                        print(f"Your New Description [{newDes}] is Successfully added")
                        print("")
                        print("*************************************************************************")
                        flag = 1
                else:
                    project_info = ":".join(project_info)
                    with open("Projects/temp.txt", "a") as notEditingFile:
                        data = project_info.strip("\n")
                        data = f"{data}\n"
                        notEditingFile.writelines(data)

            else:
                project_info = ":".join(project_info)
                with open("Projects/temp.txt", "a") as notEditingFile:
                    data = project_info.strip("\n")
                    data = f"{data}\n"
                    notEditingFile.writelines(data)

    if flag == 0:
        print("*************************************************************************")
        print(f"We can not found a title with this name [{projectTitle}]")
        print("*************************************************************************")


    os.remove("Projects/projects.txt")
    os.rename("Projects/temp.txt", "Projects/projects.txt")


# print("******************************************************************")
# print("")
# print("Press [1] if you want to editing or [0] for Exit")
# print("")
# print("******************************************************************")
# while True:
#     choise = input("Your choise is : ")
#     print("")
#     if choise.isnumeric():
#         choise = int(choise)
#         break
#     else:
#         print("Invalid Choise, Try again")






