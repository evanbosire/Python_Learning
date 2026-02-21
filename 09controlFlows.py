print(10 == 10)
print(10 != 10)
print(7 > 3)
print(3 >= 7)
print(7 <= 7)
 
# logical operators

print(3 > 1 and 5 < 1)
print(3 > 1 or 5 < 1)
print(not 3 > 1 )

# challenge
# check if a user's name is not empty and the age is greater than or equal to 18
# check if the password is at least 8 characters long and does not contain spaces
# check if a user's email is not empty, contains '@' and ends with '.com'
# check if a username is a string, is not None, and is longer than 5 characters
# check if the user is either an admin or a moderator, and either they're not banned or they've verified their email

# 1. solutiom

username = "James"
age = 18

if (username != "" and age >= 18):
    print("Condition Passed")
else:
    print("Condition Failed")


# 2. solution

password = "123456789"

if (len(password) >= 8 and password.strip() == password):
    print("Password is 8 characters long with no spaces")
else:
    print("Password is either less than 8 characters or has spaces")

# 3. solution

userEmail = "brian@gmail.com"

if userEmail and '@' in userEmail and userEmail.endswith(".com"):
    print("Condition Met")
else:
    print("Condition Failed.")

# 4. solution

username = "Brian"


if (isinstance(username, str) and username is not None and len(username) >= 5):
    print("Condition met")
else:
    print("Condition not fulfilled")

# 5. solution

admin = False
moderator = True
banned = False
emailVerified = True

if (admin or moderator) and (not banned or emailVerified):
    print("Passed")
else:
    print("Failed")





