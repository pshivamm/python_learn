a = ["Rohan", "Sohan", False, 3.89, 456]

print(a[0])
print(type(a[0]))
a[1] = "Mohit"
print(a[1])
print(a[1:4])

# methods in list

a.append("Mohan")
a.insert(3, True)
print(a)

b = [34, 45, 9, 50, 13, 66]

# b.sort()
# print(b)
# b.reverse()
# b.pop(2)
# print(b)
b.remove(9)
print(b)

e = sum(b)
print(e)