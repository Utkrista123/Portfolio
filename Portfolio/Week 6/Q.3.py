'''Write and test a function that determines if a given integer is a prime number. A
prime number is an integer greater than 1 that cannot be produced by multiplying
two other integers.'''

def is_prime(number):
    """Determine whether the input number is prime or not."""
    for i in range(2, number):
        if number % i == 0:
            print(f"The {number} is not prime number.")
            break
    else:
        print(f"The {number} is prime number.")


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        if number < 2:
            print(f"{number} is not a prime number")

        else:
            is_prime(number)

    except ValueError:
        print("Invalid input")