

def main():
    email_and_name = {}
    email = input("Enter email: ")
    while email != "":
        name = get_name(email)
        check = input("Is this your name {}? (Y/N) ".format(name))
        if check.upper != "Y" and check != "":
            name = input("Name")
        email_and_name[email] = name
        email = input("Enter email: ")
    for email, name in email_and_name.items():
        print("{} ({})".format(name, email))


def get_name(email):
    symbol = email.split("@")[0]
    parts = symbol.split(".")
    name = " ".join(parts).title()
    return name
