'''Modify your "greetings" program so that the first letter of the name entered is
always in uppercase with the rest in lowercase. This should happen even if the user
entered their name differently. So if the user entered arthur, ARTHUR, or even
arTHur the name should be displayed as Arthur.'''

def get():
    greetings = input(f"Enter you name: ")
    return greetings

def display(greet):
    if greet == {}:
        print("Hello stranger")
        
    else:
        greet = greet.capitalize()
        print(f"Hello {greet}. How are you?")

greet = get()
display(greet)

