'''Write and test a function that takes an integer as its parameter and returns the
factors of that integer. (A factor is an integer which can be multiplied by another to
yield the original).'''

def get_factors(num):
    factors = []
    for i in range(1, abs(num) + 1):
        if num % i == 0:
            factors.append(i)
    return factors

if __name__ == "__main__":
    try:
        num = int(input("Enter an integer: "))
        result = get_factors(num)
        print(f"The factors of {num} are: {result}")
    except ValueError:
        print("Invalid input")
