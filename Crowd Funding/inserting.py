def insert(userInfo):
    userInfo = ":".join(userInfo)
    with open("Users/USERS.txt", "a") as userFile:
        data = userInfo.strip("\n")
        data = f"{data}\n"
        userFile.write(data)
        print("*************************************************************************")
        print("")
        print("You Have Register Successfully, You will back to Main Menu to login......")
        print("")
        print("*************************************************************************")


# insert("mohamed32")

# with open("Users/USERS.txt", "a") as userFile:
#     data = userInfo.strip("\n")
#     data = f"{data}\n"
#     userFile.write(data)
#     print("*************************************************************************")
#     print("")
#     print("You Have Register Successfully, You will back to Main Menu to login......")
#     print("")
#     print("*************************************************************************")
