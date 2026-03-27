# 1. Write a python program to display a user entered name followed by Good
# Afternoon using input () function.

name = input("Enter your name: ")
print("Good Afternoon, "+name+"!")
print(f"Good Afternoon, {name}!")  # Using f-string for formatting

# 2. Write a program to fill in a letter template given below with name and date.
letter = '''
Dear < |Name|>,
You are selected!
< |Date| >'''

print(letter.replace("< |Name|>", "Shivam").replace("< |Date| >", "25-07-2002"))

# 3. Write a program to detect double space in a string.
text = "This is a  good boy."
print(text.find("  "))

# 4. Replace the double space from problem 3 with single spaces.
print(text.replace("  ", " "))

# 5. Write a program to format the following letter using escape sequence characters.
letter = "Dear Harry, this python course is nice. Thanks!"

formatted_letter = "Dear Harry, \n\tthis python course is nice. \nThanks!"
print(formatted_letter)