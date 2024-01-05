'''Write a program that displays the "Seven Times Table". That is, the result of
multiplying 7 by every number from 0 to 12 inclusive. The output might start:
0 x 7 = 0
1 x 7 = 7
2 x 7 = 14
and so on.'''

for i in range (0,13):
    multiplication = 7 * i
    print(f"7 x {i} = {multiplication} ")

