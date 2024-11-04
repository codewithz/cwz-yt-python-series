# {key:value,key:value,..}


# Multiple Ways of Making a Dictioanry

point={"x":1,"y":2}
print(point)
print(type(point))

point =dict(x=1,y=2)
print(point)
print(type(point))

details=dict(name="Tom",age=25,gender="Male",isMarried=False,city='Pune',programmingLanguages=['Java','Python','Rust'])
print(details)

# Accessing the elements in Dictionary

print("Name:",details.get("name"))
print("Age:",details["age"])
# print("City:",details["city"])
# KeyError: 'city'
print("City:",details.get("city"))
print("City:",details.get("city","Mumbai"))


# Add and Remove Elements from Dictionary

details["country"]="India"
print(details)

details["age"]=30
print(details)

details["programmingLanguages"].append("JS")
print(details)

del details["isMarried"]
print(details)

city=details.pop("city")
print(city)
print(details)


# Iterating through a dictionary
print(40*'-')
for key in details:
    print(key)

print(40*'-')
for element in details.items():
    key,value=element
    print(element)
    print(key,"--",value)

print(40*'-')
for key,value in details.items():
    print(key,"--",value)
    
    
