# Example 2: List of integers
numbers = [10, 20, 30, 40]

# Adding
numbers.append(50)
numbers.extend([60, 70])           # add multiple

# Math with list
total = sum(numbers)
avg = total / len(numbers)

# Sorting
numbers.sort()                     # in-place sort
numbers_rev = sorted(numbers, reverse=True)  # new sorted list

# Filtering (example: keep only even numbers)
evens = [x for x in numbers if x % 2 == 0]

print("Numbers list:", numbers)
print("Total:", total)
print("Average:", avg)
print("Even numbers:", evens)
print("Reversed sorted:", numbers_rev)