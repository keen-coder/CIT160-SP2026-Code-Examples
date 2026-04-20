# This program demonstrates keyword-only function arguments.

def main():
    total = sum(1, 2, 3, 4)
    print(total)

def sum(a, b, c, d, /):
    return a + b + c + d

if __name__ == '__main__':
    main()