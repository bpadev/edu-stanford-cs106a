# CS106A - Lecture 13 - String Parsing, Code Style, and Ethics Guest Lecture


# Readable Code
# - Different situations call for different goals, but an excellent all purpose goal for code is that it is readable. 
# - Need good function names! (Principles Of Least Surprise, functions should do what their names suggest, so other programmers are not confused when a function deletes a bunch of files but the name was log_this())
# - If function returns boolean value, start function name with is_ or has_
# - Need good variable names!


# Python Style Decomposition
# - The difficulty of completing a software project of N lines seems to be proportionate to N^2.
# - CS has this one trick to avoid the N^2 trap. Divide and Conquer. 
# - The abstraction of a function is what it accomplishes.
# - The implementation detail of a function is all the code and complexity within the function that actually does the work.
# - The point is that the abstraction is much simpler than the implementation.
# - """Pydoc describes what the function does"""
def del_chars(s, target):
  """
  Given string s and a "target" string,
  return a version of s with all chars that
  appear in target removed, e.g. s 'abc'
  with target 'bx, returns 'ac'.
  >>> del_chars('abc', 'acx')
  'b'
  >>> del_chars('ABc', 'aCx')
  'B'
  """


# Bits and Bytes
# - A "bit", like an atom, the smallest unit of storage.
# - A bit stores just a 0 or 1
# - In a chip: electric charge = 0/1
# - Group 8 bits together to make 1 byte.
# - One byte can store one roman character, e.g. 'A' or 'x' or '$'
# - Number of patterns of bits is expontential. e.g. 1 Bit has 2 Patterns, 2 Bits have 4 Patterns, 8 Bits have 256 Patterns.
# - CPU, RAM and Persistent Storage. CPU does work, RAM stores the work (temporarily), Persistent Storage keeps state even if powered-off.
# - Running a program gets its own area in RAM. Running program = "process"
# - Operating System (OS) manages CPU, RAM, etc.
# - CPU Cores can run code independently. Ex. running crypto.py on one and another might be running Chrome at the same time.
# - A core can switch from one process to another, suspending the first process and starting the second. In this way, your computer "runs" 100 programs simultaneously.
# - RAM is a big array of bytes, read and written by the CPU.
# - RAM stands for Random Access Memory (random access meaning can access any byte at will)