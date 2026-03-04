
# Action Function

def write_log(message):
    with open(r"E:\Documents\app.log", "a") as file:
        file.write(message + "\n")

#write_log("App started")
write_log("User logged in")
write_log("App stopped")


# clean up functions

def clean_name(name):
    clean_email = name.strip().lower()
    username, domain = clean_email.split('@')
    return {username, domain}

print(clean_name('evanbosire422@gmail.com'))

# validation functions

# check if the length of pass is 8
def is_valid_password(password):
    return len(password) >= 8

print(is_valid_password('1234456'))
print(is_valid_password('123445678'))

# check whether an email has a basic valid format

def is_valid_email(email):
    return "@" in email and '.' in email

print(is_valid_email('evan@gmail.com'))



# Orchestrator functions -> controls flow of your program by calling other functions


def orchastrator_process_email(email):
    write_log("App Started")

    if not is_valid_email(email):
        write_log(f"Invalid Email received: {email}")
    else:
        clean_email = clean_name(email)
        write_log(f"Processed Email: {clean_email}")
    write_log("App Stopped")


email = input("Please enter your Email: ")
orchastrator_process_email(email)