# CS106A - Lecture 6 - Even More Images


# Rwo Math Systems - int and float
# - int stores an integer.
# - floats store floating point values.
my_float = 3.14
# - Indexing is accessing an element inside something.
# - Ints are naturally used for indexing.
# - A float input makes a float output
1.5 + 1.5 # will equal 3.0
# - Python uses typical math operators and follows typical precedence.
+ - * / **
# - Unlike most languages Python int values do not have a fixed "max".
7 // 2 # int division, will evaluate to an int


# Functions - Parameters
# - A parameter to a function provides some extra data to use when the function runs.
def darker_left(filename, left):
  ...
  ...
  ...
# - Function call supplies to the actual arguments, these match the formal parametrs by position.
darker_left('poppy.jpg', 25)

