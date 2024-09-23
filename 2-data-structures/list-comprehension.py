cart= [
        ('Bread',15,2),
        ('Butter',7,3),
        ('Jam',23,1),
    ]

# ("Product","Price","Qty")

print("Cart : ",cart)

prices=list(map(lambda item:item[1],cart))

print("List of Prices:",prices)

# Map 
# [expression for item in items]

prices_lc=[item[1] for item in cart]

print(prices_lc)

# Filter 
# [expression for item in items if condition]

items_with_price_greater_than_9=[item for item in cart if item[1]>9]

print("Items greater than 9 USD",items_with_price_greater_than_9)

names=["Tom","Alex","Mike","Leonard","Sheldon"]


len_list=[len(name) for name in names]

print("Names",names)

print("Lenght",len_list)


# -----------------------------------Challenge-------------------------------------------------------
employees=[
    (1,"Tom","IT",30000),
    (2,"Alex","Accounts",33000),
    (3,"Mike","Finance",43000),
    (4,"John","HR",39000),
    (5,"Penny","IT",45000)
]

#  Q1 -- Find the list of departments in employees list
# Q2 -- find those employees whose salary is greater than 32k and work in IT


