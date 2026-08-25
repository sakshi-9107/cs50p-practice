x = int(input("what's X ? "))
y = int(input("what's Y ? "))

# if statement
if x < y :
    print(" X is less than Y")
if x > y :
    print(" X is greater than Y")
if x == y :
    print(" X is equal to Y")

# elif statement
if x < y :
    print(" X is less than Y")
elif x > y :
    print(" X is greater than Y")
elif x == y :
    print(" X is equal to Y")

# elif else statement
if x < y :
    print(" X is less than Y")
elif x > y :
    print(" X is greater than Y")
else :
    print(" X is equal to Y")

# is x equal to y or not ?
# case 1:
if x < y or x > y :
    print("x is not equal to y")
else :
    print("x is equal to y")
# case 2:
if x != y :
    print("x is not equal to y")
else :
    print("x is equal to y")
# case 3:
if x == y :
    print("x is equal to y")
else :
    print("x is not equal to y")