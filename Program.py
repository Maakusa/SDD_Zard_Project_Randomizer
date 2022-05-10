file = open("accounts.txt", 'a+')

def create_a_file():
    global file
    global fname
    global sname


    for i in range(0 ,1):
        fname = input("Please enter the first name for the first person: ")
        file.write(f'{fname}\n')


        sname = input("Please enter the surname for the first person: ")
        file.write(f'{sname}\n')


        emailaddr = input("Please enter the email address for the first person: ")
        file.write(f'{emailaddr}\n')


        mobile = input("Please enter the mobile number for the first person: ")
        file.write(f'{mobile}\n')

    file.close()
def display_file_contents():
    file = open("accounts.txt", 'r')
    details = file.readlines()
    counter = 0

    for i in range(0, int(len(details)/4)):
        fname = details[counter]
        counter += 1
        sname = details[counter]
        counter += 1
        emailaddr = details[counter]
        counter += 1
        mobile = details[counter]
        counter += 1
        print(fname + sname + emailaddr + mobile)



def add_new_record():
    print("Please enter the details for the first new person to be added:")
    print("Please enter xxx for both first name and surname to indicate there are no more record to be added")

    fname = input("First name: ")
    sname = input("Surname: ")
    emailaddr = input("Email Address: ")
    mobile = input("Mobile Number: ")

    while fname != "xxx" and sname != "xxx":
        file.write(f'{fname}\n')
        file.write(f'{sname}\n')
        file.write(f'{emailaddr}\n')
        file.write(f'{mobile}\n')

        print("Please enter the details for the first new person to be added:")
        print("Please enter xxx for both first name and surname to indicate there are no more record to be added")

        fname = file.readline()[-4]
        sname = file.readline()[-3]
        emailaddr = file.readline()[-2]
        mobile = file.readline()[-1]
        continue



while True:

    control = input("Enter 'c' to create a record, 'd' to display record, 'a' to add to the records or 'q' to close the program: ")

    if control == 'c':
        create_a_file()

    if control == 'd':
        display_file_contents()

    if control == 'a':
        add_new_record()

    if control == 'q':
        file.close()
        exit()

    else:
        continue



