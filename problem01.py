# 1. Write a program to print Twinkle twinkle little star poem in python.

print('''All Nashville is a chill. And everywhere
Like desert sand, when the winds blow,
There is each moment sifted through the air,
A powdered blast of January snow.''')

# 2. Use REPL and print the table of 5 using it. (in the terminal)

# 3. Install an external module and use it to perform an operation of your interest.
import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say('''All Nashville is a chill.''')
engine.runAndWait()

# 4. Write a python program to print the contents of a directory using the os module. Search online for the function which does that.
import os
directory_path= '/'

contents = os.listdir(directory_path)
for item in contents:
    print(item)


# 5. Label the program written in problem 4 with comments. (already commented)