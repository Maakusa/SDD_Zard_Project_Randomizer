from random import randint


def login():
    #take username input
    #check if username is on the list and retreive password for said username
    #prompt password input
    #check password with input
    #return true or false
    return True



def register(): 
    # Function prompts user for a username and password, giving them the option to randomly generate one
    # after which it repeats to them their username and password before writing them to a file.

    usernameFile = open("usernames.txt", 'a+')
    passwordFile = open("passwords.txt", 'a+')
    accountFile = open("accounts.txt", 'a+')

    username = input("Please enter a username: ")
    password = ""

    userIn = input("Either enter a password or leave blank to generate a randomized password: ")

    if userIn == "":
        userIn = input("Enter a key: l = letter, n = number, s = symbol (ie: lns for letters numbers and symbols): ")
        length = input("Enter password length: ")
        userIn = userIn.lower()
        if "l" in userIn or "n" in userIn or "s" in userIn:
            password = passGen("l" in userIn, "n" in userIn, "s" in userIn, int(length))
        else:
            print("Invalid input, generating password with letters, numbers and symbols of 16 characters length.")
            password = passGen(True, True, True, 16)
    else:
        password = userIn

    print("Username: ", username)
    print("Password: ", password)
    accountFile.write("Username: " + username + " Password: " + password + "\n")
    usernameFile.write(username + " ")
    passwordFile.write(password + " ")

    usernameFile.close()
    passwordFile.close()


def passGen(randLet, randNum, randSym, len):
    # Generates a random password based on the choice of symbols numbers or letters and the length

    genPass = ""

    if randLet and randNum and randSym:
        for i in range(len):
            r = randint(1, 3)
            if r == 1:
                genPass += genRandLet()
            elif r == 2:
                genPass += str(randint(0, 9))
            else:
                genPass += genRandSym()

    elif (randLet and randNum) or (randNum and randSym) or (randSym and randLet):
        if randLet and randNum:
            for i in range(len):
                r = randint(1, 2)
                if r == 1:
                    genPass += genRandLet()
                else:
                    genPass += str(randint(0,9))
        elif randLet and randSym:
            for i in range(len):
                r = randint(1, 2)
                if r == 1:
                    genPass += genRandLet()
                else:
                    genPass += genRandSym()
        else:
            for i in range(len):
                r = randint(1, 2)
                if r == 1:
                    genPass += genRandSym()
                else:
                    genPass += str(randint(0,9))

    else:
        if randLet:
            for i in range(len):
                genPass += genRandLet()
        elif randNum:
            for i in range(len):
                genPass += str(randint(0,9))
        else:
            for i in range(len):
                genPass += genRandSym()
    return genPass


def genRandLet():
    genned = str(chr(randint(65, 90)))
    r = randint(1, 2)
    if r == 1:
        genned = genned.lower()
    return str(genned)


def genRandSym():
    r = randint(33, 64)
    if r > 60:
        r += 62
    elif r > 54:
        r += 36
    elif r > 47:
        r += 10
    return str(chr(r))
    


def viewAccounts():
    accountFile = open("accounts.txt", 'r')
    print(accountFile.read())
    accountFile.close()



def deleteAccounts():
    accountFile = open("accounts.txt", 'w')
    usernameFile = open("usernames.txt", 'w')
    passwordFile = open("passwords.txt", 'w')
    accountFile.write("")
    usernameFile.write("")
    passwordFile.write("")
    accountFile.close()
    usernameFile.close()
    passwordFile.close()



#BEGIN Main
x = True # flag for mainLoop
logged = False # boolean for being logged in
userChoice = "" # choice of user for operation

while x:


    if logged: #Menu for being logged in
        userChoice = input("Choose your operation: (v = view accounts, e = exit, d = delete all accounts) ").lower()
        if userChoice == "v":
            viewAccounts()
        elif userChoice == "e":
            x = False
        elif userChoice == "d":
            deleteAccounts()
        else:
            print("Please input a valid operation.")

    else: #Menu for users trying to log in
        userChoice = input("Choose your operation: (l = login, r = register, e = exit) ").lower()
        if userChoice == "l":
            logged = login()
        elif userChoice == "r":
            register()
        elif userChoice == "e":
            x = False
        else:
            print("Please input a valid operation.")
