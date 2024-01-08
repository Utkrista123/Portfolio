'''Write a program that reads 6 temperatures (in the same format as before), and
displays the maximum, minimum, and mean of the values.
Hint: You should know there are built-in functions for max and min. If you hunt, you
might also find one for the mean.'''

from statistics import mean
def get():
    new_list = []
    for _ in range (1,7):
        temperature = float(input("Enter temperature: "))
        new_list.append(temperature)
    return new_list

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


temp = get()
max = calculate_max(temp)
min = calculate_min(temp)
means = caluculate_mean(temp)
display(max, min, means)