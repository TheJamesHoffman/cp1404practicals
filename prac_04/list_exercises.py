numbers = []
score = 0
while score != 5:
    user_score = int(input("Please enter a number: "))
    numbers.append(user_score)
    score = score + 1
print("Number: ", numbers)
print("your first number is ", numbers[0])
print("your last number is ", numbers[4])
print("your smallest number is ", min(numbers))
print("your largest number is ", max(numbers))
list_average = sum(numbers) / len(numbers)
print("the average of the list", list_average)

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
input_name = input("please enter your username: ")
check_username = -1
username_found = True

while username_found:
    try:
        check_username = usernames.index(input_name, check_username + 1)
    except ValueError:
        username_found = False

if check_username == -1:
    print("Access denied")
else:
    print("Access granted")