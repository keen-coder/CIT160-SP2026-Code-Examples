
def main():

    # For now, you don't need to understand exactly what is happening here.
    # You just need to understand enough to be able to adapt this example for
    # any program where you want to read multiple values from the console in
    # one line.

    # Example reading integers:
    num1, num2, num3 = map(int, input('Enter three values separated by spaces: ').split())

    # Example reading floats:
    num1, num2, num3, num4 = map(float, input('Enter four values separated by spaces: ').split())

    # Example reading strings:
    # NOTE: This only works if your strings are all one word, if you are reading
    # strings with multiple words per string you can't use this method. It will
    # be better to read one string per line (the way you know how).
    str1, str2, str3, str5, str5 = input('Enter five words separated by spaces: ').split()

    # NOTE: You can change the mapped function between int and float depending
    # on what values you are reading. 
    #
    # Reading multiple words does not require the use of the map() function.
    # If you want to read more or less values, just add or remove the correct
    # number of variable names to the left of the assignment (=)

if __name__ == '__main__':
    main()

