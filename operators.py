# 1. Arithmetic operators: +, -, *, / etc.
a = 2
b = 5
c = a + b

print(c)

# 2. Assignment operators: =, +=, -= etc.
a = 4 + 5
b = 5
b += 5
c = a + b

print(c)

b -= 3

print(b)

# 3. Comparison operators: ==, >, >=, <, != etc.
a = 5 > 4
b = 5 < 4
c = 5 <= 6
d = 5 != 5
e = 5 == 5

print(e)

# 4. Logical operators: and, or, not

e = True or False
print(e)

print("True or True is", True or False)
print("True or False is", True or False)
print("False or True is", True or False)
print("False or False is", True or False)

e = True and False
print(e)

print("True and True is", True and False)
print("True and False is", True and False)
print("False and True is", True and False)
print("False and False is", True and False)

print(not(False))
print(not(True))