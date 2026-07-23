# we don't pass parameter in function hello() so that we can't write hello(name) 
# if we write hello(name) it returns error
def hello():
    print("hello, ")
    
name = input("what's your name? ")
hello()
print(name)
# hello(name) wrong 

# passing parameter to function
def welcome(to):
    print("welcome to", to)

welcome("SPPU")       #with in-built argument
clg = input("what's your college name? ")
welcome(clg)

# passing default argument NA
def branch(br="NA"):
    print("Your branch is", br)

branch()            # calling without argument
b_name = input("what's your branch name? ")
branch(b_name)      # calling with argument
 

# returning value
def add(a, b):
    return a + b

result = add(2, 3)
print(result)