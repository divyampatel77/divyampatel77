# Program 5: Grocery billing system
prices = {"apple": 50, "banana": 20, "milk": 30}
quantities = {"apple": 2, "banana": 5, "milk": 1}
total_bill = sum(prices[item] * quantities.get(item, 0) for item in prices)
print("Total Bill Amount:", total_bill)
