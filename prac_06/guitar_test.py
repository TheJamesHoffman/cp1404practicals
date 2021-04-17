from prac_06.guitar import Guitar


def test_guitar():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    alt_guitar = Guitar("Another Guitar", 2013, 425)

    print("{} get_age() - expected {} got {}".format(guitar.name, 99, guitar.get_age()))
    print("{} get_age() - expected {} got {}".format(alt_guitar.name, 8, alt_guitar.get_age()))

    print("{} is_vintage() - expected {} got {}".format(guitar.name, True, guitar.is_vintage()))
    print("{} is_vintage() - expected {} got {}".format(alt_guitar.name, False, alt_guitar.is_vintage()))


if __name__ == '__main__':
    test_guitar()
