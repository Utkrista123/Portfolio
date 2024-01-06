'''Last week you wrote a program that processed a collection of temperature readings
entered by the user and displayed the maximum, minimum, and mean. Create a
version of that program that takes the values from the command-line instead. Be
sure to handle the case where no arguments are provided!'''

import sys
from statistics import mean
def get(value):
    try:
        new_list = [float(temperature) for temperature in value]
        
        return new_list
    
    except EOFError:
        print("Invalid input please try again.")

def calculate_max(temp):
    # maximum = temp[0]
    # for i in temp:
    #     if i > maximum:
    #         maximum = i

    maximum = max(temp)

    return maximum

def calculate_min(temp):
    # minimum = temp[0]
    # for i in temp:
    #     if i < minimum:
    #         minimum = i

    minimum = min(temp)

    return minimum

def caluculate_mean(temp):
    # sums = sum(temp)
    # means = sums / len(temp)
    means = mean(temp)
    return means

def display(max, min, means):
    print("The maximum value is: ",max)
    print("The minimum value is: ",min)
    print("The mean value is: ",means)


if __name__ == "__main__":

    if len(sys.argv ) >= 2:
        value = sys.argv[1:]
        temp = get(value)
        
    else:
        print("Invalid input!!!")

    max = calculate_max(temp)
    min = calculate_min(temp)
    means = caluculate_mean(temp)
    display(max, min, means)