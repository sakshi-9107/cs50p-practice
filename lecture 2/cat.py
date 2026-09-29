# LOOPS 
print("meow")
print("meow")
print("meow")

# using while loop
i = 3
while i!= 0:
    print("meow.")
    i = i -1 

i = 1
while i <= 3:
    print("meow..")
    i = i + 1

i = 0
while i < 3:
    print("meow...")
    i += 1

# using for loop
for i in [0, 1, 2]:
    print("meow....")

for i in range(3):
    print("meow.....")

for _ in range(3):
    print("meow")

# using multiplication
print("meow." * 3)

print("meow.\n" * 3)

print("meow..\n" * 3, end="")

# improving with user input 
while True:
    n = int(input("what's n? "))
    '''
    if n < 0:
        continue   #"what's n? " asking user till user don't enter postive value 
    else:
        break      #comes out from this loop after entering positive value 
    '''
    # more easy way to write above committed section
    if n > 0:
        break
for _ in range(n):
    print("meow...")

# using define (def()) function
def main():
    meow(3)
def meow(n):
    for _ in range(n):
        print("meow....")
main()
# but what if we want to input from user code is follows
def main():
    meow(get_number())
def get_number():
    while True:
        n = int(input("what's n? "))
        if n > 0:
            break
    return n 
def meow(n):
    for _ in range(n):
        print("meow.....")
main()
