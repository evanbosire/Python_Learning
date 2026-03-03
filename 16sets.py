# Lists -> are unordered collection of unique values

my_set = {10, 30, 20}   # sets are unordered
my_set2 = {10, 30, 20, 10}   # sets does not allow duplicates
my_set2 = {10, 30, 20, 10}   # sets are not indexed
my_set2.remove(20)  # sets are mutable

print(my_set)
print(my_set2)

# Set Methods

a = {10, 20, 30, 40}

a.add(50) # accepts a number to add to the set
a.update([1,2]) # with update you can pass anything even a list, set or number

# removing item from a set

a.remove(10) # we can remove by item since no index
a.discard(100) # does the same job like remove but does not break if the item to remove does not exist

print(a)


# mathematical operators in sets

a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

print(a.union(b)) # or
print(a | b) 
print(a.intersection(b)) # gives the shared items only
print(a.difference(b)) # gives items only in a that are not shared with b
print(a.symmetric_difference(b)) # gives all items that are not shared btn a and b 

# relationship btn sets

print(a.issubset(b)) # will return true if all elements in a are in b
print(b.issuperset(a))
print(a.isdisjoint(b)) # returns trues if no shared values


