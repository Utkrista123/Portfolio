'''Modify the "Times Table" again so that the user still enters the number of the table,
but if this number is negative the table is printed backwards. So entering "-7"
would produce the Seven Times Table starting at "12 times" down to "0 times".'''

number = int(input("Enter a number: "))

if number > 0:
    for i in range (0,13):
        multiplication = number * i
        print(f"{number} x {i} = {multiplication} ")

elif number < 0:
    for i in range (13, 0, -1):
        multiplication = number * i
        print(f"{number} x {i} = {multiplication} ")
