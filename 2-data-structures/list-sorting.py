numbers=[3,1,15,65,0,43]

numbers.sort()

print('Sorted:',numbers)
print('Original:',numbers)

print('-------- Reverse Sorting ------------')

numbers.sort(reverse=True)
print('Reversed:',numbers)

# -----------------------------------------------

other_numbers=[0,23,21,45,87,24,90]

sorted_numbers=sorted(other_numbers)

print('O:',other_numbers)
print('Sorted:',sorted_numbers)

# ------------------------------------------------
print('-------- Sorting Complex Objects ------------')
# -------('Product, Price, Quantity) ---------------------
cart= [
        ('Bread',15,2),
        ('Butter',7,3),
        ('Jam',23,1),
    ]

def key_for_cart(item):
    #  ('Bread',15,2),
    return item[1];


cart.sort(key=key_for_cart,reverse=True)

print('Sorted Cart',cart)

def key_for_total_price(item):
    #  ('Bread',15,2),
    return item[1]*item[2];

cart.sort(key=lambda item:item[1]*item[2])
print('Sorted Cart on Total Price',cart)

def key_for_cart(item):
    #  ('Bread',15,2),
    return item[1];

# sorting_on_price= lambda item:item[1];

cart.sort(key=lambda item:item[1])
print(cart)