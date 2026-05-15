# Homework 2
text = input("Enter your text: ")

# 1. Length of text (Characters)
c = len(text)

# 2. Split and count words
w = len(text.split())

# 3. Count punctuation for sentences
s = text.count('.') + text.count('?') + text.count('!')

# Output results
print("Characters:", c)
print("Words:", w)
print("Sentences:", s)