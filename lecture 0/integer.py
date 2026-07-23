# in-built values
x = 3
y = 2
z = x+y
print(z)

# user input
x = input("what's x? ")
y = input("what's y? ")

a = x+y        #concatination happens due to + sign it indicates to concat strings and even if they are numbers but they act like a string 
print(f"a={a}")

b = int(x) + int(y)            #actual addition takes place
print(f"b={b}")

# storing user input in the form of integer to make it more easy
x = int(input("what's x? "))
y = int(input("what's y? "))
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)

# check if no. is integer or not
isinstance(25, int)
isinstance(543.1212, int)