MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = celsius_to_fahrenheit()
        elif choice == "F":
            fahrenheit_to_celsius(celsius)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def fahrenheit_to_celsius(celsius):
    fahrenheit = float(input("Fahrenheit: "))
    fahrenheit = celsius * 5 / 9.0 - 32
    print("result: {:.2f} C".format(celsius))


def celsius_to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))
    return celsius


main()
