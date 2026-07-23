def main():
    name = input("what's your name? ")
    hello(name)

    x = int(input("what's x? "))
    print("x squared is", square(x))

    a = float(input("what's a? "))
    b = float(input("what's b? "))
    print("addition of a and b is", add(a, b))

def hello(to="world"):
    print("hello",to)

def square(n):
    return n ** 2

def add(x, y):
    return x + y

main()