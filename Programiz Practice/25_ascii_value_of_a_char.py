def check():
    char = input("Enter a character: ")

    if len(char) > 1:
        print("Please enter only 1 character")
        check()
    else:
        print(f"ASCII of {char} = {ord(char)}")

check()

