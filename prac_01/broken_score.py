"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
while score > 100 or score < 0:
    print("invalid score")
    score = float(input("enter score: "))
if score >= 50:
    print("passable")
if score > 90:
    print("excellent")
if score < 50:
    print("bad")
