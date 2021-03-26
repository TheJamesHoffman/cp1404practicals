import random

RANDOM_NUMBER_DISPLAY = 6
MIN = 1
MAX = 45

number_of_picks = int(input("How many quick picks? "))


for i in range(number_of_picks):
    quick_picks = []
    for j in range(RANDOM_NUMBER_DISPLAY):
        number = random.randint(MIN, MAX)
        while number in quick_picks:
            number = random.randint(MIN, MAX)
        quick_picks.append(number)
    quick_picks.sort()
    print(" ".join("{:2}".format(number) for number in quick_picks))
