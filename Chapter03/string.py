# # 1.String slicing example

# a = "johns"

# print(a[0:3])

# print(a[-4: -1])

# print(a[:4])

# print(a[2:])

# b = "chinese"

# print(b[1:5:2])

# c = "1234567890"

# print(c[1:6:3])
# print(c[::-1])


# 2. String Methods example
d = " Hello, World! "

# print(len(d))
# print(d.endswith("ld! "))
# print(d.startswith("ld! "))
# print(d.capitalize())
# print(d.count("o"))

# print(d.strip())          # Remove whitespace from both ends
# print(d.lower())          # Convert to lowercase
# print(d.upper())          # Convert to uppercase
# print(d.replace("H", "J"))  # Replace substring
# print(d.split(","))      # Split string into a list
# print(d.title())   # Find substring index
# print(d.find("world"))
# print(d.index("world"))
# print(d.isalpha())       # Check if all characters are alphabetic
# print(d.isdigit())       # Check if all characters are digits
# print(d.islower())       # Check if all characters are lowercase
# print(d.isupper())       # Check if all characters are uppercase
# print(d.isspace())       # Check if all characters are whitespace
# print(d.swapcase())      # Swap case of characters

print(d.center(3))     # Center the string within a specified width
print(d.replace("o", "8")) # Replace occurrences of a substring with another substring
print(d.join(["A", "B", "C", "D"]))  # Join elements of an iterable with the string as a separator