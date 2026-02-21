name = "Brian"

print(type(name))

# Types
age = 24
print(type(age))  # -> type()
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
print(number.replace("+", "00").replace(" ",
      "").replace("-", "").replace("(", "").replace(")", ""))

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

print(
    f"My name is {name}, I am {age} years old, and student status is {is_student}")

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

# lstrip() -> removes white spaces from the left
# rstrip() -> removes white spaces from the right
# strip() -> removes white spaces from both sides.

text = " Engineering"
text = "Engineering "
text = " Engineering "
text = "###Abc##"

print(text.lstrip())
print(text.rstrip())
print(text.strip())
print(text.strip("#"))  # -> When passing args to the strip method,
#    it removes those characters from a string


#   Case Conversions
text = "python PROGRAMMING"

print(text.lower())
print(text.upper())
print(text.capitalize())    # First letter capital

# challenge
# "968-Maria, ( D@t@ Engineer ) ;; 27y  " -> name: maria | role: data engineer | age: 27

# solution
text = "968-Maria, ( D@t@ Engineer ) ;; 27y  "
print(text.strip().replace("@", "a"))
name = text.strip()[4:9].lower()
role = text.strip()[13:26].lower().replace("@", "a")
age = text.strip()[-3:-1].lower()

print(f"name: {name} | role: {role} | age: {age}")

print("#" * 60)


text1 = "968-Maria, ( D@t@ Engineer ) ;; 27y"
print(f"{text1}")
clean = text1.replace("@", "a").strip()
print(clean)
# Split parts
id_name, rest = clean.split(",", 1)

print(id_name, rest)

role_part, age_part = rest.split(";;")
print(role_part, age_part)


# String Searching


date = "2026-Feb-10"
url = "https://api.company/v1/data"
phone1 = "+48-176-12345"
phone2 = "48-654-16548"
phone3 = "0048-654-16548"

print(date.startswith("2026"))
print(date.endswith("10"))
print("Feb" in date)
print(f"Find 10 is at index: {date.find("10")}")
print("/api" in url)

print(phone1[4:])
print(phone2[3:])
# solution instead of counting the indexes

print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])
print(phone3[phone3.find("-")+1:])

# String functions validation

country = "KENYA"
phone = "012367654"

print(country.isalpha())    # checks is the string has only alphabets a-z A-Z
print(phone.isnumeric())    # checks if phone is a number
