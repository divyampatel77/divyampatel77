# Program 5
tuples = [(), (1, 2), (), (3, 4)]
non_empty = [t for t in tuples if t]
print("After removing empty tuples:", non_empty)
