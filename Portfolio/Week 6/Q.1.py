'''Write a function that accepts a positive integer as a parameter and then returns a
representation of that number in binary (base 2).'''

def decimal(num):
    number = ''
    while num > 0:
        number = str(num % 2) + number
        num = num // 2
    print(number)
    
if __name__ == "__main__":
    num = int(input("Enter a positive integer: "))
    if num < 0:
        print("Please enter a positive integer.")
    else:
        decimal(num)