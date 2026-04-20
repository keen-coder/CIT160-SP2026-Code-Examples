# This program displays a count-down.

def main():
    print('Beginning countdown.')

    count = 10
    while count > 0:
        print(count)
        count -= 1

    print('Blastoff!')


if __name__ == '__main__':
    main()
