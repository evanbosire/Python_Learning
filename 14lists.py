import copy

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

# list functions

numbers = [1, 5, 2, 4, 3]

print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))
print("Length:", len(numbers))

print("All:", all(numbers)) # -> you will get True if the list contains all numbers
print("All:", all([1, 0, 2]))   # 0 is considered as empty value
print("All:", all(['a', '', 'b']))   # "" is considered as empty value also


print("All:", any(numbers)) # -> will return True if we have at least 1 element in the list
print("All:", any([1, 0, 2]))
print("All:", any([0, 0, 0])) # -> false since 0 is treated as empty


print("Count:", numbers.count(5)) # -> counts the occurences of 5
print("Index:", numbers.index(5)) # -> returns position(index) for the first occurence of number 5


print(4 in numbers) # using membership operator


# Adding elements to the list

letters = ['a', 'b', 'c']
letters.append('x') # -> adds elements at the end of the list
letters.insert(0, 'z') # -> adds elements at specified indexes

print(letters)


# Removing elements from a list

letters = ['a', 'b', 'c', 'a']
#letters.clear() # -> removes everything
letters.remove('a') # -> searches for 'a' and removes 1st occurence
letters.pop() # -> by default removes the last element if not given index and returns removed item

print(letters)


# Updating items in a list


names = ['john', 'james', 'ben']
names[0] = 'Jane'

print(names)


# Sorting a items in a list

alphabets = ['c', 'a', 'b']
alphabets.sort()    # sorts in ascending order
print(alphabets)

alphabets.sort(reverse=True)    # sorts in descending order
print(alphabets)

# sorted function

new_list = sorted(alphabets)

print("Original list:",alphabets)
print("Sorted list:",new_list)

# Reversing a list

letters3 = ['c', 'a', 'b']
print("Original list:", letters3)

letters3.reverse()
print("Reversed list:", letters3)


# copying a list

originalList = ['a', 'b', 'c']

# shallow copy
copiedList = originalList.copy()
copiedList.append('z')

print(originalList)
print(copiedList)

# deep copy -> Needs to import a new module


matrix = [
    ['a', 'b'],
    ['c', 'd']
]

matrix_copy = copy.deepcopy(matrix)
matrix.pop()
matrix_copy[0].append('z')
print("Original Matrix:", matrix)
print("Copy Matrix = ", matrix_copy)


# combining data in lists

lettersList = ['a', 'b', 'c']
numbersList = [1, 2, 3]

combination = lettersList + numbersList
combination2 = [lettersList, numbersList]
numbersList.extend(lettersList)

print(combination)
print(combination2)
print(numbersList)

# combining lists using zip() -> used to pair elements from all lists and returns an iterator which we can convert into a list of tuples

lettersList = ['a', 'b', 'c']
numbersList = [1, 2, 3]
comb = zip(lettersList, numbersList)

print(list(comb))

#  Example of zip()

ids = [101, 102, 103]
names = ['Ali', 'Sara', 'John']

print(list(zip(ids, names)))


# Iterating through a list

lettersList = ['a', 'b', 'c']

for l in lettersList:
    print(l)


# enumerate -> gives the value and its index while looping

lettersList = ['a', 'b', 'c']

print(list(enumerate(lettersList)))

for index, value in enumerate(lettersList):
    print(index, value)


# Reveresed -> returnss an iterator that flips the data order

letters = ['a', 'b', 'c']
print(list(reversed(letters)))

for l in reversed(letters):
    print(l)


# zip() -> combines two or more sequences into pairs (tuples)

numbers = [1, 2, 3]


for l, n in (zip(letters, numbers)):
    print(l, n)


# map

letters = ['a', 'b', 'c']
numbers = ['1', '2', '3']

print(list(map(str.upper, letters)))
print(list(map(int, numbers)))


# filter -> used in cleaning up data

letters = ['a', 'b',None, '', 'c', False]
items = ['sql', '123', 'python', '42']

print(list(filter(None, letters)))
#   OR
print(list(filter(bool, letters)))
print(list(filter(str.isalpha, items))) # filters only alphabets


for i in filter(str.isalpha, items):
    print(i)


# lambda functions

multiply = lambda x: x*2

print(multiply(2))


add = lambda x, y: x + y
print(add(1,2))

check = lambda i: i in "python"

print(check('z'))


# lambda + map

prices = ['$12.50', '$9.99', '$100.00']

print(list(map(lambda p: float(p.replace('$', '')), prices)))


# lambda + filter

prices = [120, 30, 300, 80] # remove all prices lower than 100
students = [['Maria', 85],
            ['Kumar', 90],
            ['Max', 60]]    # list where student score is higher than 70

print(list(filter(lambda p: p >= 100, prices)))
print(list(filter(lambda row: row[1] > 70, students)))
print(list(filter(lambda row: 'M' in row[0]  , students)))








