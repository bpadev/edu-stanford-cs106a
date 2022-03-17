# CS106A - Lecture 19 - Dictionaries Part 2


# Dict
# - when Python uses an assignment - with a data structure like a list or a dict, Python does not make a copy of the structure.
# - instead there is just the one list or dict, and multiple pointers pointing to it.


# Hosts Problem

# - input
emails = ['hi@benjamin.dev', 'ben@benjamin.dev', 'hi@mayflower.agency']

# - solution
def email_hosts(emails):
  hosts = {}
  for email in emails:
    at = email.find('@')
    user = email[:at]
    host = email[at + 1:]

    # key algorithm: init/increment
    if host not in hosts:
      hosts[host] = []
    users = hosts[host] # decomp by var
    users.append(user)
  return hosts

print(email_hosts(emails))