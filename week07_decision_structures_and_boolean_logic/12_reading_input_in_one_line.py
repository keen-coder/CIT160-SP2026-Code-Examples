
def main():

    # For now, you don't need to understand exactly what is happening here.
    # You just need to understand enough to be able to adapt this example for
    # any program where you want to read multiple values from the console in
    # one line.
    num1, num2, num3 = map(int, input('Enter three values separated by spaces: ').split())

    print(num1)
    print(num2)
    print(num3)

    # Below is the same work as above, just split into multiple lines.



if __name__ == '__main__':
    main()

