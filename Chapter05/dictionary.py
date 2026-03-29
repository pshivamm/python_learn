marks = {
    "shivam": 89,
    "rohan": 78,
    "sohan": 90,
    "mohan": 56,
    "list": [1, 2, 3, 4],
}

print(marks,type(marks))
print(marks["shivam"])

#mehtods in dictionary

print(marks.keys())
print(marks.values())
print(marks.items())
marks.update({"shivam": 99, "rohan": 88})
print(marks)

print(marks.get("shivam"))
# print(marks.get("shivam1")) it will return None because there is no key with the name "shivam1".
# print(marks["rohan1"]) it will give an error because there is no key with the name "rohan1".

# print(marks.clear())
print(marks.copy())

new_dict = dict.fromkeys(["a", "b", "c"], 0)
print(new_dict)

key = ["e", "f", "g"]
new_dict1 = dict.fromkeys(key, 55)
print(new_dict1)
