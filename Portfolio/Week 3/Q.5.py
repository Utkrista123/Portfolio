'''Modify your program a final time so that it executes until the user successfully
chooses a password. That is, if the password chosen fails any of the checks, the
program should return to asking for the password the first time.'''

a = 1
while a == 1:
    new_password = input("Enter a new password: ")
    confirm_password = input("Confirm your password: ")

    if new_password == 'password' or 'letmein' or 'sesame' or 'hello' or 'justinbieber':
            print("This is a bad Password")

    if new_password == confirm_password and 8 < len(new_password) <= 12:
        print("Password Set")
        break

    if len(new_password) <= 8 or len(new_password) >= 12:
        print("Please use 8 to 12 characters for Password.")

    if new_password != confirm_password:
        print("Error Password does not match")

    confirmation = input("Do you want to redo it (Y/N): ")
    confirmation.upper()

    if confirmation == "Y":
         continue
    else:
         print("Thank You for your time")
         break