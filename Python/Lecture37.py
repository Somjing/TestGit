usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput  == "admin":
    if passwordInput == "1234":
        print("Login Success !")
    else:
        (print("Password incorrect"))
else:
    print("Username or Password incorrect")