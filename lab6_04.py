# Program 4
items = [("Burger", 50), ("Pizza", 100), ("Sandwich", 30)]
items.sort(key=lambda x: x[1], reverse=True)
print("Sorted items by price (desc):", items)
