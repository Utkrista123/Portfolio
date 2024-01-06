'''Write and test a function that converts a temperature measured in degrees
centigrade into the equivalent in fahrenheit, and another that does the reverse
conversion. Test both functions. '''

def get():
    temperature = float(input("Enter the temperature: "))
    unit_of_temperature = input("Enter the unit of the temperature(c/f): ")
    unit_of_temperature = unit_of_temperature.lower()
    return(temperature, unit_of_temperature)

def calculate_faherenheit(temp):
    faherenheit = (temp*9/5)+32
    return(faherenheit)

def calculate_centigrade(temp):
    centigrade = ((temp-32)*5)/9
    return (centigrade)

def display(FC, CF, u_temp):
    if u_temp =="c" or u_temp == "centigrade":
        print("The value in centigrade is: ",CF)
    elif u_temp == "f"or u_temp == "faharenheit":
        print("The value in faherenheit is: ",FC)

    else:
        print("!!! Invalid value !!!")

temp, u_temp = get()
FC = calculate_faherenheit(temp)
CF = calculate_centigrade(temp)
display(FC, CF, u_temp)