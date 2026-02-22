# Create Lists

empty = []
letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]
letters2 = list("Python")
mixed = [1, 'a', True, None]
matrix = [['a', 'b', 'c'], 
          ['d', 'e', 'f']]

print(empty)
print(type(letters))
print(numbers)
print(letters2)
print(mixed)
print(matrix)

# Accessing & Reading a List

lst = letters = ['a', 'b', 'c', 'd']

matrix = [['a', 'b', 'c'], # Row 0
          ['d', 'e', 'f'], # Row 1
          ['g', 'h', 'i']] # Row 2


# print(lst[0])
# print(lst[-1])
# print(matrix)
print(matrix[-1])
print(matrix[-1][-1])

# Slicing in Lists

print(lst[:2])
print(lst[2:])
print(lst[:])

# Unpacking

person = ['Maria', 29, 'Data Engineer', 'Kenya']
# name = person[0]
# age = person[1]
# role = person[2]
# country = person[3]

name, age, role, country = person   # unpacking in play

print(name)
print(age)

# Asterisk* in unpacking

name, *details, country = person

print(name)
print(details)
print(country)

# underscore in unpacking to skip what we are not interested in

name, _, role, _ = person

print(name)
print(role)

# combining * with _ in unpacking

name, *_, = person
print(name)

