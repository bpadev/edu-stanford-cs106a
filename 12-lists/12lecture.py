# CS106A - Lecture 12 - Lists


# General
# - Don't write code for something Python has built in.
# - Foreach loop
# s = 'Hello'
# for ch in s:
#   # do this
#   print(ch);


# Lists
# - A list is a linear collection of any type of python value.
# - Lists can contain any type of element.
# - Lists are mutable, unlike strings, lists can be changed.
# lst = ['a', 'b', 'c']
# lst.append(1)
# 'c' in lst

# donut_index(foods)
foods = ['fruit', 'pizza', 'pasta']
def donut_index(foods):
  if 'donut' in foods:
    return foods.index('donut')
  return -1

print(donut_index(foods))
# - CONSTANTS, intended to be a read-only value
STATES = ['MA', 'FL', 'NH']
# - main() will have args setup in a list 
args == ['-affirm', 'Lisa']
