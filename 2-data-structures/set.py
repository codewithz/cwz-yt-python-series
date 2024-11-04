# Set -- {}

numbers= {1,2,3,4,5,6,7,5,5,5,7,7,7,99,9,2,3}
print(numbers)

# Define Sets 

first=set(numbers)
print(type(first))
print(first)

second= {1,4,5}
print(type(second))
print(second)

# Operations on Set 

# Add and Removing

second.add(6)
print(second)

second.remove(4)
print(second)

second.discard(4)
print(second)

# second.remove(4)
# print(second)

print(40*'-')
print("----------- SET OPERATIONS-----------------")

# UNION -- union  |
# INTERSECTION -- intersection &
# DIFFERENCE -- difference -
# SYMMETRIC DIFFERENCE symmetric_difference ^ 

first={1,2,3,4,5,6}
second={3,4,5,6,7,8,9}

print("First:",first)
print("SECOND:",second)

print("----------UNION------------")

union_one=first.union(second)
union_two=first|second
print("Union-1:",union_one)
print("Union-2:",union_two)

print("----------INTERSECTION------------")

inter_one=first.intersection(second)
inter_two=first & second
print("intersection 1:",inter_one)
print("intersection 2:",inter_two)


print("------------DIFFERENCE and SYMMETRIC DIFFERENCE-------")
difference_one=first.difference(second)
print(difference_one)
difference_two=second - first
print(difference_two)

sym_diff_one=first.symmetric_difference(second)
print(sym_diff_one)
sym_diff_two=first ^ second
print(sym_diff_two)