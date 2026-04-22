# This program divides a number by another number.

def main():
    # Get two numbers.
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    print(divide(num1, num2))

def divide(num1, num2):
    # Divide num1 by num2 and display the result.
    result = num1 / num2
    print(f'{num1} divided by {num2} is {result}')


# Call the main function.
if __name__ == '__main__':
    main()