# This program demonstrates keyword-only arguments.

def main():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    print('Your name reversed is')
    reverse_name(last_name, first_name)

def reverse_name(first, last, /):
    print(last, first)

if __name__ == '__main__':
    main()