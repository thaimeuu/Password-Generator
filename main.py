import random
import string


def password_generator(length, isnum, isspecial, isspace):
    letters = string.ascii_letters

    nums = string.digits
    special = string.punctuation
    space = " " * 10  # 10 spaces to save time

    if isnum == "y":
        letters += nums
    if isspecial == "y":
        letters += special
    if isspace == "y":
        letters += space

    characters = random.sample(letters, k=len(letters))

    password = ""
    has_nums = False
    has_special = False
    has_space = False
    met_criteria = False

    while len(password) < length or not met_criteria:
        char = random.choice(characters)
        password += char

        if char in nums:
            has_nums = True
        if char in special:
            has_special = True
        if char in space:
            has_space = True
        if has_nums + has_special + has_space == (isnum == 'y') + (isspecial == 'y') + (isspace == 'y'):
            met_criteria = True

    return password


def main():
    while True:
        length = input(
            "How many characters AT LEAST do you want to generate? (at least 4): "
        )
        if not length.isdigit() or int(length) < 4:
            print("Try again!")
            continue
        isnum = input("Do you want to have numbers? (y/n): ").lower()
        isspecial = input("Do you want to have special characters? (y/n): ").lower()
        isspace = input("Do you want to have whitespace? (y/n): ").lower()
        print("\nYour password is generated successfully!")
        print(
            f"<your_password>: <{password_generator(int(length), isnum, isspecial, isspace)}>"
        )
        break


if __name__ == "__main__":
    main()
    print("")
