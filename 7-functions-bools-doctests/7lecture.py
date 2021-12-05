# CS106A - Lecture 7 - Functions & Parameters, Booleans, Strings, and Doctests


# Functions
# - Each function is like a little "black box" of some computation, with data-in and data-out.
# - Can return a value from a function.
def winnings1(score):
  return score * 10
# - None is the default return value of a function.
# - Keep cases in mind.


# Booleans
# - Boolean value is True or False.
# - Boolean operator combines values in an expression.
and or not 


# Strings
# - String is a sequence of "characters" or "chars".
# - A string written in code is called a "literal".
len('hello') # returns number of chars in string.
# - Strings can be empty. Important edge case to keep in mind.
s = 'Python'
s[0] # 'P'
# - A string in memory is not editable (immutable).
