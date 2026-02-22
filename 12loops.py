# for loop

items = (1,2,3,4,5,6)
for item in items:
    print(f"Round: {item}")

print("*" * 50)
for item in range(5):
    print(f"Round: {item}")

print("*" * 50)
for item in range(1, 5): # we have 1 as the start
    print(f"Round: {item}")

print("*" * 50)
for item in range(1, 10, 2): # we have 2 as the step
    print(f"Round: {item}")

# example 1 find the sum

scores = [80, 50, 60, 75]
total = 0

for score in scores:
    total += score
    print("Current Total:", total)
print("Final Total:", total)

# example 2 transform data

files = [" Report.csv", "DATA.csv ", " final.TXT"]

for file in files:
    file = file.strip().lower().replace(".txt", ".csv")
    print(f"Processing {file}")

# challenge print 7- times table from 1 to 10 using for loop
for i in range(1, 11):
    print("7 * ", i, "=", 7 * i)
    

# print a left-aligned pyramid of stars with 6 rows using for loop

for i in range(1, 7):
    print("*" * i)

# break statement

names = ["john", "maria", "", "kumar"]

for name in names:
    if name == "":
        print("Empty value detected")
        break
    print(f"Name = {name}")

print("#" * 50)

# continue statement

names = ["john", "maria", "", "kumar"]

for name in names:
    if name == "":
        print("Empty value detected")
        continue
    print(f"Name = {name}")

# pass statement

names = ["john", "maria", "", "kumar"]

for name in names:
    if name == "":
        print("Empty value detected")
        pass # todo: Handle Empty Value
    print(f"Name = {name}")


# challenge skip weekends in calender loop

days = ["Mon", "Sun", "Wed", "Tue"]
weekends = ["Sat", "Sun"]
for day in days:
    if day in weekends:
        continue
    print(f"Workday: {day}")

# else + break in loops

items = [1, 3, 4, 7]

for i in items:
    if i % 2 == 0:
        print("Even number found",i)
        break
else:
    print("All numbers are odd")


files = ['data1.csv',
         'report.pdf',
         'report2.csv']

for file in files:
    if not file.endswith(".csv"):
        print(f"{file} is not a CSV")
        break
else:
    print("All files are CSV")


# check whether any filename appears more than once
# print "Duplicate found" if a duplicate exists, otherwise print "All files are unique"

file_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',
    'data.csv'
]
new_list = []

for file in file_list:
    
    if file in new_list:
        print(f"Duplicate found, {file}")
        break
    else:
        new_list.append(file)
else:
    print("All files are unique")


# Write a program that:
# Checks if any username is invalid
# A username is invalid if:
# It is shorter than 5 characters, OR
#It contains a space " ".  


usernames = [
    "brian23",
    "john doe",
    "alex99",
    "mary_ann",
    "sam"
]

for username in usernames:
    if len(username) < 5 or " " in username:
        print(f"Invalid username found: {username}")
        break
else:
    print("All usernames are valid")


# Nested Loops

for x in range(3): # outer loop
    for y in range(2): # inner loop
        for z in range(2):
            print(f"{x}, {y}, {z}")

print("#" * 50)

# challenge generate each colors with each size

colors = ['red', 'blue', 'green']
sizes = ['L', 'M', 'S']

for color in colors:
    for size in sizes:
        print(f"{color} - {size}")
print("#" * 50)

# SELECT count(*) FROM customers where id IS null

tables = ['customers', 'orders', 'products', 'prices']
columns = ['id', 'create_date']

for t in tables:
    for c in columns:
        print(f"SELECT count(*) FROM {t} WHERE {c} IS NULL;")


print("*" * 50)

# While loop 

# while condition

count = 1

while count <= 5:
    print(count)
    count += 1


# write a program that keeps asking "Do you agree?" until the user types "yes"


answer = ""
while answer != "yes":
    answer = input("Do you agree? (yes/no): ")
print("Thank you.")

# while True

while True:
    answer = input("Do you agree? (yes/no): ")
    if answer == "yes":
        break
print("Thank you")


# challenge
# 3 attempts
# Yes within three attempts -> "Glad we're on the same page"
# Otherwise "3 strikes. You're out!"

attempts = 0
while attempts < 3:
    answer = input("Do you agree? (yes/no): ")
    if answer == "yes":
        print("Glad we're on the same page")
        break
    attempts += 1
else:
    print("3 strikes. You're out!")









