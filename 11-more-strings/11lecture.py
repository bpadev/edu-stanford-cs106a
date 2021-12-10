# CS106A - Lecture 11 - More Strings


# Types
# - Integers (int), Floats (float), Strings (str)
my_int = 123
my_str = 'Benjamin'
# - Can convert as well
print(type(int('848484')))
print(type(str(my_int)))


# Files
# - A text file is a series of lines. Each line is a series of chars ending with a '\n' char.
open(filename) # open for reading, most common
open(filename, 'r') # same as above, 'r' denotes reading
open(filename, 'w') # open for writing