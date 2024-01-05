'''Write a program that simulates the way in which a user might choose a password.
The program should prompt for a new password, and then prompt again. If the two
passwords entered are the same the program should say "Password Set" or
similar, otherwise it should report an error.'''

new_password = input("Enter a new password: ")
confirm_password = input("Confirm your password: ")

if new_password == confirm_password:
    print("Password Set")

else:
    print("Error Password does not match")