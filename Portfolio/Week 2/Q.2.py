'''Write a program that prompts a user to enter a temperature in Celsius, and then
displays the corresponding temperature in Fahrenheit, like so:
Enter a temperature in Celsius: 32.5
32.5C is equivalent to 90.5F.'''

temp_in_Celsius = float(input("Enter the temperature in Celsius: "))
temp_in_Fahrenheit = (temp_in_Celsius * 9/5) + 32
print("The temperature in Faharenheit is: ",temp_in_Fahrenheit)