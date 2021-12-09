# Given string s, return a string of its digit chars.'
test = 'Hi4x3hhfhf647fhfht8t848484hhh'

def digits_only(str):
  result = ''

  for i in range(len(str)):
    if not str[i].isalpha():
      result += str[i]

  return result

print(digits_only(test));