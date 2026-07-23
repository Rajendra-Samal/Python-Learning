tasks = ["email", "call", "review", "deploy"]

while tasks:
    current = tasks.pop(0)  # remove from front
    print("Processing:", current)

print("All tasks done.")