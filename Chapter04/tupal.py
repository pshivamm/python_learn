a = () #empty tuple
print(type(a))

b= (1, 2, 3, 4, 5)
print(b[0])
#print[3] = 5 Because it is immutable and it cannot be change like string

# Methods in tuples

c = (1, 2, 3, 4, 5, 2, 3)

print(c.count(2))
print(c.index(4))

d = (1, 2, 3, 4, 5)

e = c + d
print(e)
repeat = d * 3 #repeat the tuple d three times
print(repeat)

print(len(e)) #length of the tuple e

print(3 in e) # check the value it will return True if it is present.
print(10 in e) # check the value it will return False if it is not present.

