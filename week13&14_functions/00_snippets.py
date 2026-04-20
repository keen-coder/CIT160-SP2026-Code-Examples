

def main():
    # my_function1(1, 2, 3, 4) # Postional Arguments
    # my_function1(a=1, b=2, c=3, d=4) # Keyword Arguments
    # my_function1(c=3, a=1, d=4, b=2) # Keyword Arguments

    # my_function2(1, z=10)
    # my_function2(1, 2, z=10)
    # my_function2(1, 2, 3)
    # my_function2(1, 2, 3, 4)

    my_function1(1, 2, c=3, d=4)


# Function without default values
def my_function1(a, b, *, c, /, d):
    print(a, b, c, d)

def my_function2(w=0, x=0, y=1, z=0):
    print(w, x, y, z)





if __name__ == '__main__':
    main()