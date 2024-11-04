#  ()

point =(1,2)
print(type(point))
print(point)

point=1,2
print(type(point))
print(point)

point =1,
print(type(point))
print(point)

# Operations with Tuple 

tuple1=(1,2)
tuple2=(3,4)
tuple3=tuple1+tuple2
print(tuple3)

ones=(1,)*10
print(ones)

cwz=("cwz",)*4
print(cwz)

# Packing and Unpacking in a Tuple 

packed_tuple=1,2,3,4

print(type(packed_tuple))
print(packed_tuple)

point_3_d=(3,6,9)

x,y,z=point_3_d
print("x: ",x)
print("y: ",y)
print("z: ",z)


# Accessing the elements in tuple

point=(1,2,3,3,4,5,6,7)

print("Index 2: ",point[2])

print("Range Access:",point[0:3])

print("Index 4 :",point.index(4))

print("Count of 3:",point.count(3))

# If i try to makechanges to a tuple 

# point[1]=6
# Traceback (most recent call last):
#   File "J:\Zartab\CodeWithZAcademy\Python-Series\2-data-structures\tuples.py", line 57, in <module>
#     point[1]=6
#     ~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

