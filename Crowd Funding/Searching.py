def recordSearching(usermail, title):
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
                    print(f"********************* Project Data You search for **********************")
                    print(f"User Email: {project_info[0]}")
                    print(f"Project Title: {project_info[1]}")
                    print(f"Description: {project_info[2]}")
                    print(f"Total target: {project_info[3]}")
                    print(f"Start Date: {project_info[4]}")
                    print(f"End Date: {project_info[5]}")
                    print("*************************************************************************")
                    flag = 1

    if flag == 0:
        print("*************************************************************************")
        print(f"We can not found a title with this name [{projectTitle}]")
        print("*************************************************************************")



#
# recordSearching("mohamed2@gmail.com", "rrr")
