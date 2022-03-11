# CS106A - Lecture 18 - Dictionaries Part 1


# Dict
# - a key/value dictionary
# - in CS generally known as a "hash table"
# - job interview pattern: Interview question has some messed up data, Best answer inevitably uses a dict to organize the data, Because the dict is powerful and fast..., Interviewers cannot resist using it
# - organize data around keys.
# - all dict logic is on the key, the value is just stored.
d = {'a': 'arsenault', 'b': 'bennito', 'c': 'caliente'}
'a' in d
# "in" guard pattern, only access key/values if the key exists.

