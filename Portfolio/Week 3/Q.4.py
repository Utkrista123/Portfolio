'''Modify your program again so that the chosen password cannot be one of a list of
common passwords, defined thus:
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']'''

new_password = input("Enter a new password: ")
confirm_password = input("Confirm your password: ")

if new_password == 'password' or 'letmein' or 'sesame' or 'hello' or 'justinbieber':
        print("This is a bad Password")

elif new_password == confirm_password and 8 < len(new_password) <= 12:
    print("Password Set")

elif len(new_password) <= 8 or len(new_password) >= 12:
    print("Please use 8 to 12 characters for Password.")

elif new_password != confirm_password:
    print("Error Password does not match")
