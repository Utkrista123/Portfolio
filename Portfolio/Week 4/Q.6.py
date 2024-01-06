'''Write a program that takes a centigrade temperature and displays the equivalent in
fahrenheit. The input should be a number followed by a letter C. The output should
be in the same format.'''

def get():
    temperature = float(input("Enter the temperature: ")) 
    print(f"The value in centigrade is: {temperature} C")
    return(temperature)

def calculate_faherenheit(temp):
    faherenheit = (temp*9/5)+32
    return(faherenheit)

def display(CF):
        print("The value in faherenheit is: ",CF,"F")

temp = get()
FC = calculate_faherenheit(temp)
display(FC)









