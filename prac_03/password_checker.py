MIN_LENGTH = 2
symbol = "*"


def main():
    user_password = get_password()
    password_length = len(user_password)
    if password_length > MIN_LENGTH:
        print_symbols(password_length)
    else:
        print("Password is too short")


def print_symbols(password_length):
    print(symbol * password_length)


def get_password():
    print("enter a valid password")
    print("your password must be longer then", MIN_LENGTH)
    user_password = input("> ")
    return user_password


main()
