'''Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long.'''

new_password = input("Enter a new password: ")
confirm_password = input("Confirm your password: ")

if new_password == confirm_password and 8 < len(new_password) <= 12:
    print("Password Set")

elif len(new_password) < 8 or len(new_password) >= 12:
    print("Please use 8 to 12 characters for Password.")

elif new_password != confirm_password:
    print("Error Password does not match")
