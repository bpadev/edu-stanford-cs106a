# CS106A - Lecture 1 - Code and Bit


# Basics
# - The computer is stupid. You must tell it exactly what to do.
# - A computer program or "app" is a collection of code for the computer to run. 
# - The code in a program is divided into smaller, logical units of code called functions.
def main(a, b):
  ...
  ...
  ...


# Bit Robot - Getting Started
# - Running a function is also known as "calling" that function.
# - Functions are usually verb like, separated by underscores. 
def parse_data(file, format):
  ...
  ...
  ...


# Statement vs. Expression
# - A line of Python code may be a statement or an expression.
# - A statement runs code that performs an action.
bit.move()
# - An expression runs code and returns a value to that spot.
bit.front_clear() # returns a boolean, needs to be evaluated, not telling anyone what to do.


# While Loops
while test-expression:
  ...
  ...
  ...
  # do this until text-expression != true


# One Code - Many Cases - Generality
# - General, it should work for all the different input worlds.