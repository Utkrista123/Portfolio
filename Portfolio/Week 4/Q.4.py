'''When processing data it is often useful to remove the last character from some
input (it is often a newline). Write and test a function that takes a string parameter
and returns it with the last character removed. (If the string contains one or fewer
characters, return it unchanged.)'''

def get():
    """Asks for user input and removes the last character if necessary."""
    user_string = input("Enter a string: ")
    return user_string

def calculate(word):
    if len(word) <= 1:
        return(word)

    else:
        return(word[:-1])
    
def display(result):
    print("The string is: ",result)
    
word = get()
result = calculate(word)
display(result)