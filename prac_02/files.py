# Question 1

output_file = "name.txt"
out_file = open(output_file, 'w')
username = input("Please enter your name: ")
print(username, file=out_file)
out_file.close()

# Question 2
out_file = open(output_file, "r")
name_str = out_file.readline()
print("Your name is {}".format(name_str))
out_file.close()

# Question 3
file_numbers = open("numbers.txt")
number1 = int(file_numbers.readline())
number2 = int(file_numbers.readline())
print(number1 + number2)
file_numbers.close()

# Question 4
count = 0
file_numbers = open("numbers.txt")
for line in file_numbers:
    count += 1
print(count)
