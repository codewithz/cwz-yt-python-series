# lists -- [] -- mutable -- indexed 

letters= ['a','b','c','d','e']
print(letters)
print(type(letters))


matrix = [[0,1],[2,3]]
print(matrix)

zeros =10*[0]
print(zeros)

combined=letters+zeros
print(combined)

name='Code With Z'
chars=list(name)
print(chars)


# ---- Access the elements in list ----
#         0    1   2   3   4
letters= ['a','b','c','d','e']
#         1    2   3   4   5
print('First Element',letters[0])
print('Last Element',letters[-1])

# Acccess in Ranges 

print(letters[0:2])
print(letters[:3])
print(letters[2:])

# Clone 

letters_clone=letters[:]
print(letters_clone)

# Steppers
numbers=list(range(1,21))
print(numbers)

print(numbers[::2])
print(numbers[::1])
print(numbers[::-1])

# -- List Unpacking 

numbers= [1,2,3,4,4,4,4,5,6]

# first =numbers[0]
# second=numbers[1]
# second_last=numbers[-2]
# last=numbers[-1]

f,second,*others,second_last,last=numbers

print('First',f)
print('Second',second)
print('Second Last',second_last)
print('Last',last)
print('Others',others)


letters=['a','b','c','d','e']

for letter in letters:
    print(letter)

print(40*'-')

for element in enumerate(letters):
    print(element)

print(40*'-')

element=(1,'b')
index,value=element
print(index,'--',value)

print(40*'-')

for index,value in enumerate(letters):
   print(index,'-->',value)