# is number is even or odd ?
x = int(input("what's x? "))

# using modulo(%)
if x % 2 == 0 :
    print(x,"is even")
else:
    print(x,"is odd")

# using parity function
def main():
    y = int(input("what's y? "))
    if is_even(y):
        print(y,"is even")
    else:
        print(y,"is odd")

# case 1:
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# case 2: use of pythonic
def is_even(n):
    return True if n % 2 == 0 else False

# case 3: use of pythonic 
# it makes code simple 
def is_even(n):
    return (n % 2 == 0)
main()



print(True + True)   # 2
print(False + 5)     # 5
print(True == 1)     # True
print(False == 0)    # True
print(True + 5)      # 6