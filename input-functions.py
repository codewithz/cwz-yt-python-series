name=input("Enter your name:")
age=input("Enter your age:")

print(name,"--",age)
print(type(name),"--",type(age))

age=int(age)
print(type(name),"--",type(age))

print(f"Hey {name} , you are {age} years old")
print(f"Next year, you will be {age+1} years old")