"""
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is
displayed on the screen.
"""
cost = 0
item = int(input("How many items: "))

for i in range(item):
    cost += float(input("Enter cost of each item: $ "))
print("total cost for the", item, "items are $", cost)
