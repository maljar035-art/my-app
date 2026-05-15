 # Homework 4

# 1. Define the list
nums = [1, 5, 2, 5, 3, 5, 4]

# 2. The number we want to search for
target = 5

# 3. Counter variable
count = 0

# 4. Loop through the list
for x in nums:
    if x == target:
        count = count + 1

# 5. Print result
print("The number", target, "appeared", count, "times")  