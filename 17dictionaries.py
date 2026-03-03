my_dict = {
    'a': 10,
    'b': 20,
    'c': 30,
    'a': 40
}

print(my_dict)  # dict is ordered | no duplicates for keys | Not indexed but keyed instead
print(my_dict['b'])

my_dict['c'] = 80 # mutable

print(my_dict)


#   dict methods

user = {'id': 1, 'age': 30, 'city': 'Kenya'}

# print(user['name']) # not safe way to check existence since it breaks code instead use get()
print(user.get('name'))

#checks for keys
print('age' in user)

#view objects
print(user.keys())
print(user.values())
print(user.items()) # keys with values

# lopping

for u in user:
    print(u, user[u])

# modern way of looping

for key, value in user.items():
    print(key, value)


# Add, Remove, Update

user['name'] = 'John' # Add
print(user)
user['age'] = 35 # Update
print(user)
user.update({'age': 40, 'city': 'Paris'}) # allows many updates
print(user)
user.pop('age', 'Not Found') # removes item from a dict
print(user)
user.popitem() # removes last item in the dict
print(user)


# creating dictionaries

user = {
    'id': None,
    'name': None,
    'age': None,
    'city': None,
}
# NB: instead of repeating None we can do:

user = dict.fromkeys(['id', 'name', 'age', 'city'], None)
print(user)

user = {'id': 1, 'name': 'John', 'age': 30, 'city': 'Berlin'}
user_str = {
    #Expression
    k: v.upper()
    #Loop
    for k, v in user.items()
    #Filter
    if isinstance(v, str)
}

print(user_str)













