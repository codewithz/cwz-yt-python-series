if True:
    print("Condition is True")
else:
    print("Condition is False")

print(40*'-')

number=3

if(number%2==0):
    print("Even Number")
else:
    print("Odd Number")


# Operators 

# > -- Greater Than
# >= -- Greater Than equals
# < -- Less Than
# <=  -- Less Than equals
# == --equals
# != -- Not equals

print(40*'-')
a=100
b=200

if(a>b):
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")

print(40*'-')


# and
# or
# not 

# Loan processing system 

high_income=False
good_credit=True
is_student=True 

print(40*'-')

if high_income and good_credit:
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")


print(40*'-')

if (high_income or good_credit) and is_student:
    print("Eligible for Loan")
else:
    print("Not Eligible for loan")

print(40*'-')
print("Ternary Operator")

age=17

# if age>18:
#     print("Eligible Age")
# else:
#     print("Non eligible age")


message= 'Eligible Age' if (age>18) else 'Non eligible age'
print(message)

print(40*'-')

# age should be between 18 and 65 

if age>18 and age<65:
    print("Elgible Age")

if 18 <= age <= 65:
    print("Elgible Age with chaion operator")


