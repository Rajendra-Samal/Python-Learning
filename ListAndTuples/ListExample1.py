# Example 1: List of strings
names = ["Alice", "Bob", "Charlie"]

# Adding elements
names.append("Diana")              # add to end
names.insert(1, "Anna")            # insert at index 1

# Modifying
names[0] = "Alicia"

# Removing
names.pop()                        # remove last
names.remove("Anna")               # remove first "Anna"

# Slicing
print("Names list:", names)
print("Slice names[1:3]:", names[1:3])

