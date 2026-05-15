# Homework 3
numbers = []
for i in range(5):
    num = float(input("Enter a number: "))
    numbers.append(num)

total = sum(numbers)
average = total / 5
largest = max(numbers)

print("Total:", total)
print("Average:", average)
print("Largest:", largest)