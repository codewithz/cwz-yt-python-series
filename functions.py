def greet():
    print('Hi There')
    print('Welcome to Python Functions')

# -------------------------------------------------------
greet()

# --------------------------------------------------------

def add_two_numbers(one,two):
    print(one,'+',two,'=',(one+two))

# ----------------------------------------

add_two_numbers(1,3)
add_two_numbers(20,10)
add_two_numbers(10,4)
add_two_numbers(0,0)

# ----------------------------------

# FUnctions can or cannot return
# Do some process
# return something

def get_greetings(name):
    return 'Hi '+name+" . Welcome to Code With Z!!"
# ---------------------------------------
message=get_greetings('Zartab')
print(message)

# Send this in an email
# Save to DB
# Store in a file 
# Send over network
# Feed it to a AI Model 

# -------------- Keyword Arguments ---------------

import math 

def increment_after_factorial(number,by):
    factorial=math.factorial(number)
    add_to_factorial=factorial+by
    return add_to_factorial;

# ----------------------------------------

result= increment_after_factorial(4,5)
print(result)

result=increment_after_factorial(number=5,by=7)
print(result)


# --------- Default Arguments ---------

def increment(number, by=1):
    return number+by;

# -------------------------------------------

result=increment(6)
print(result)

result=increment(number=6,by=3)
print(result)