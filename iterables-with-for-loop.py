

# for element in collection:
    # what you want to do with the element in this iteration


for character in 'Code With Z':
    print(character)

print(40*'-')

for number in [1,2,3,4,5]:
    print(number,'----Square is ----',number*number)

print(40*'-')

for x in range(1,10):
    print(x)
print(40*'-')

# for-else 

# if i break the loop in between -- it was completed
# if it completes, i have an option to handle it 

successful=False
for attempt in range(1,6):
    print('Attempting to send a message')

    if(attempt==3 and successful):
        print('Message has been sent successfully')
        break;

else:
    print('Attempted 5 times to send a message and failed')

