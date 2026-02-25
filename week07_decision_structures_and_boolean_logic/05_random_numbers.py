# Import the random module
import random

def main():
    # Generate a random integer between 1 and 10 inclusive.
    rand_int1 = random.randint(1, 10)
    print(f'Random Integer 1:\t{rand_int1}')

    # Generate a random integer between 7 and 42 inclusive.
    rand_int2 = random.randint(7, 42)
    print(f'Random Integer 2:\t{rand_int2}')

    # Generate a random float between 0.0 and 1.0 exclusive.
    rand_float1 = random.random()
    print(f'Random Float 1:\t\t{rand_float1}')

    # Generate a random float between 3.7 and 12.34 exclusive.
    rand_float2 = random.uniform(3.7, 12.34)
    print(f'Random Float 1:\t\t{rand_float2}')

    
if __name__ == '__main__':
    main()