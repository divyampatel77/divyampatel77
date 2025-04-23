# lab_8_03.py
# Add 5 new names to a set, modify one, and delete two names

names = set()
names.update(["Alice", "Bob", "Charlie", "David", "Eve"])
names.discard("Alice")
names.discard("Bob")
names.add("Alicia")  # Modified version of Alice

print("Updated names set:", names)
