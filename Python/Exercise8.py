usernameinput = input("Username : ")
passwordinput = input("Password : ")

if usernameinput == "admin" and passwordinput == "1234":
    print("Login completed.")
    print("----Fruit Shop----")
    print("-------Menu list--------")
    print("1. Orange      : 30 THB")
    print("2. Grape       : 50 THB")
    print("3. Apple       : 40 THB")
    print("---------------------------")
    userSelectedProduct = int(input("Choose Fruit Number : "))
    if userSelectedProduct == 1:
        print("1. Orange")
        userQuantityProduct = int(input(" How many pieces do you need? : "))
        print("Orange", userQuantityProduct, "Price Total:", 30 * userQuantityProduct , "THB")
    elif userSelectedProduct == 2:
        print("2. Grape")
        userQuantityProduct = int(input(" How many pieces do you need? : "))
        print("Grape", userQuantityProduct, "Price  Total:", 50 * userQuantityProduct , "THB")
    elif userSelectedProduct == 3:
        print("3. Apple")
        userQuantityProduct = int(input(" How many pieces do you need? : "))
        print("Apple", userQuantityProduct, "Price  Total:", 40 * userQuantityProduct , "THB")
    print("----Thank You----")
else:
    print("Incorrect Username/Password.")