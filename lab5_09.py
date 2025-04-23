# Program 9
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
list3 = [x for x in list1 if x not in list2]
print("List1:", list1)
print("List2:", list2)
print("Elements in List1 not in List2:", list3)
