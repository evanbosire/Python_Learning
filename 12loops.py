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