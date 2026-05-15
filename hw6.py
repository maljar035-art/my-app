 # Homework 6

def remove_duplicates(my_list):
    new_list = []
    for x in my_list:
        if x not in new_list:
            new_list.append(x)
    return new_list

# Test the function
data = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(data)

print("Original:", data)
print("New List:", result) 