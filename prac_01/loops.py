
for i in range(1, 21, 2):
    print(i, end=' ')
    print()



for i in range(0, 101, 10):
    print(i, end=' ')
    print()



for i in range (20, 0, -1):
    print(i, end=' ')
    print()


star = input("Enter the amount of stars your want: ")
symbol = "*"
for i in range(int(star)):
    print(symbol, end=' ')



star = input("Enter the amount of stars your want: ")
symbol = "*"
for i in range(1, (int(star))):
    print(symbol * i)
