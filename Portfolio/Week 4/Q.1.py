'''Functions are often used to validate input. Write a function that accepts a single
integer as a parameter and returns True if the integer is in the range 0 to 100
(inclusive), or False otherwise. Write a short program to test the function.'''

def get():
    num = float(input("Enter a number: "))
    return num

def test(number):
    if 0 <= number <= 100:
        return True
    
    else:
        return False
    
def display(result):
    print("The result is:",result)
    

number = get()
result = test(number)
display(result)