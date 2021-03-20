import random

def main():
    score = user_score()
    while score > 100 or score < 0:
        print("invalid score")
        score = float(input("enter score: "))
    if score >= 50:
        print("passable")
    if score > 90:
        print("excellent")
    if score < 50:
        print("bad")
    print(random.randint(1, 100))


def user_score():
    score = float(input("Enter score: "))
    return score


main()
