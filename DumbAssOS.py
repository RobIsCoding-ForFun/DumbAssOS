print("Wellcom to DumbAssOS")

username = input("Please enter a username; ")

if (username == "" or username.__contains__("null")):
    pass

password = input("Please enter a password for "+ username + "; ")

if (password == "" or ("null")):
    pass

print("Wellcom to DumbAssOS " + username + "!")
print("Also thanks for using the program will now shutdown")

exit()