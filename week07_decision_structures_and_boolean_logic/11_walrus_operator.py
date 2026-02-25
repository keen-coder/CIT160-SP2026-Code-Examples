
def main():
    CORRECT = "opensesame"

    # Capture once, reuse multiple times
    if not (pw := input("Enter password: ")):
        print("Password cannot be empty.")
    elif len(pw) < 6:
        print("Password too short.")
    elif pw == CORRECT:
        print("Access granted.")
    else:
        print("Access denied.")

if __name__ == '__main__':
    main()