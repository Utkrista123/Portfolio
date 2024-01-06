'''Write a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string. Test the
function with a short program'''

def get():
    sentence = input("Enter a sentence")
    return sentence

def upper(sent):
    u_count = 0
    for i in sent:
        if i.isupper():
            u_count += 1
    return u_count        

def lower(sent):
    l_count = 0
    for i in sent:
        if i.islower():
            l_count += 1
    return l_count

def display(upper_case, lower_case):
    print('Number of Upper Case Letters :', upper_case)
    print('Number of Lower Case Letters :', lower_case)

sent = get()
upper_case = upper(sent)
lower_case = lower(sent)
display(upper_case, lower_case)
