'''Modify the previous program so that it can process any number of values. The input
terminates when the user just pressed "Enter" at the prompt rather than entering a
value.'''

from statistics import mean
def get():
    new_list = []
    loop = 1
    while loop == 1:
        temperature = float(input("Enter temperature: "))
        new_list.append(temperature)
        if temperature == {}:
            continue
        elif temperature:
            break
        else:
            pass
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

def display(max, min, means,temp):
    print("The maximum value is: ",max)
    print("The minimum value is: ",min)
    print("The mean value is: ",means)


temp = get()
max = calculate_max(temp)
min = calculate_min(temp)
means = caluculate_mean(temp)
display(max, min, means)