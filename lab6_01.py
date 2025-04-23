# Program 1
data = [("John",), "Emily", ("Tom",), "Sophie", ("Mike",)]
boys = [name for name in data if isinstance(name, tuple)]
girls = [name for name in data if not isinstance(name, tuple)]
print("Number of boys:", len(boys))
print("Number of girls:", len(girls))
