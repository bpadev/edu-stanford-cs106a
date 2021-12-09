# CS106A - Lecture 9 - More Grids


# Debugging
# - 1) Look at the exception. 
# - 2) Look at the output + your code.
# - 3) Add print() in the code.
# - Reverse String
def reverse2(str):
  reverse = ''

  for i in reversed(range(len(str))):
    reverse += str[i]

  return reverse

print(reverse2('hello'))
# - A computer program is "deterministic" - each time you run the lines with the same input, they do exactly the same thing.
# - A "module" is a library of code we want to use.

