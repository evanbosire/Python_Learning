name = "Brian"

print(type(name))

# Types
age = 24
print(type(age)) # -> type()
print("Your age is:" + str(age))  # -> str()

# Math
password = "123a"
text = """
    Python is easy to learn.
    Python is powerful.
    Many people love python.
"""
print(len(password))  # -> len()
print(text.count("Python"))  # -> .count()

# Transformations
price = "1234,56"
phone = "176-1234-56"
amount = "$1,299.99"

print(price.replace(",", "."))  # -> .replace("old", "current")
print(phone.replace("-", " "))
print(amount.replace("$", "").replace(",", ""))

# Challenge
# Convert "+49 (176) 123 - 4567" to 00491761234567

number = "+49 (176) 123 - 4567"
print(number.replace("+", "00").replace(" ", "").replace("-", "").replace("(", "").replace(")", ""))

# String Concantenation

first_name = "Brian"
second_name = "Evans"
print(first_name + " " + second_name)

folder = "C:/Users/Brian"
file = "report.csv"
file = folder + "/" + file
print(file)


# f-string

name = "Brian"
age = 34
is_student = False

print(f"My name is {name}, I am {age} years old, and student status is {is_student}")

print(f"2 + 3 = {2 + 3}")

# split()

stamp = "2026-09-20"
csv_file = "1234, Max, Kenya, 1970-10-05, M"

print(stamp.split("-"))
print(csv_file.split(","))

# repetitions

print("ha" * 3)
print("=" * 50)

# String Extractions

text = "Python"
date = "2026-09-20"

print(text[0])
print(text[-1])
print(text[0: 4])
print(text[0: 4: 2])
print(date[0:4])
print(date[5:7])
print(date[-2:])

# Cleaning String Values














