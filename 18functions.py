# Functions -> reusable block of code.

def greet():
    print('Hello')

greet()

# parameters & arguments

def clean_name(name):
    print(name.strip().lower())

clean_name(" Jane ")
clean_name(" KUMAR ")

# global vs local variables

case_rule = 'lower' # -> global variable

def clean(name):
    cleaned = name.strip()
    if case_rule == "lower":
        cleaned = cleaned.lower()
   
    print('Cleaned', cleaned)
    print(cleaned) # -> cleaned is local to the func

clean('James  ')


# *args and **kwargs -> allow functions to accept a unknown number of arguments

# *args -> stands for positional arguments
# **kwargs -> stands for keyword arguments

def total(a, b, c):
    print(a + b + c)

total(1, 3, 8)

# solution to passing many same data type parameters

def total(*args):   # *args is used when passing same data types are params
    print(sum(args))

total(1,2,3,5)

# solution to passing many parameters with different params

def create_user(**kwargs):
    
    print(type(kwargs))
    print(kwargs)

create_user(first_name = "Mosalah",
            last_name= "Salah")