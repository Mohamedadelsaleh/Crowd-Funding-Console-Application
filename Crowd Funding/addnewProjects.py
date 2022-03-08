def addProject(projectInfo):
    finalInfor = ":".join(projectInfo)
    with open(f"Projects/projects.txt", "a") as projectFile:
        data = finalInfor.strip("\n")
        data = f"{data}\n"
        projectFile.write(data)
        print("*************************************************************************")
        print("")
        print("      You Have add project Successfully, You will back to Menu......     ")
        print("")
        print("*************************************************************************")
    return
