letters=['a','b','c','e']

print('Original',letters)

# Add an element

letters.append('f')

print('Appended:',letters)

# Insert element at an index 

letters.insert(3,'d')
print('After Insert ',letters)

# Remove the elements 

popped=letters.pop(0)
print('Poppped Element:',popped)
print('List after Popping:',letters)

letters.remove('e')
print('Removed:',letters)

del letters[1]
print('After Del:',letters)

numbers=list(range(1,10))
print('Numbers',numbers)

del numbers[4:6]
print(numbers)

letters= ['d','a','b','e','c']
print("Letters:",letters)

print('Index of a:',letters.index('a'))

# print('Index of f:',letters.index('f'))
#     print('Index of f:',letters.index('f'))
#                         ^^^^^^^^^^^^^^^^^^
# ValueError: 'f' is not in list

# Find but without breaking an application 

if 'f' in letters:
    print('W1:Index of f is :',letters.index('f'))
else:
    print('f is not in the list')

# Way 2 

count=letters.count('f')

if count>0:
    print('W2 :Index of f is :',letters.index('f'))
