import math
import random
#   number functions types

x = 5
y = 5.7
z = 2 + 3j

print(type(x))
print(type(y))
print(type(z))

#   converting the data types

x = "24"
y = 3

print(type(x))
x = int(x)
print(type(x))
print(float(y))

#   math operators

print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 3)
print(7 // 2)
print(7 % 2)
print(2 ** 3)

#   rounding numbers

price = 35.5355

print(abs(2 - 10)) # gets rid of negative
print(round(price))
print(round(price, 2)) # rounds to 2dp
print(math.floor(price))
print(math.ceil(price))
print(math.trunc(price)) # it will remove all the decimals but won't do ceil of floor


# Random

print(random.random())
print(random.randint(1, 6)) # generates random int in the range we specify the last one inclusive

 
randomInt = random.randint(1, 100)

if randomInt % 2 == 0:
    print(f"{randomInt} is an Even Number")
else:
    print(f"{randomInt} is an Odd Number")
    