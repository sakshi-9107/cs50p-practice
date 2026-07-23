def main():
    name = input("what's your name? ")
    hello(name)


def hello(to="world"):
    print("hello",to)

main()

# returning value
def main():
    x = int(input("what's x? "))
    print("x squared is", square(x))

def square(n):
    return n*n
    # return pow(n, 2)
    # return n ** 2

main()

def main():
    a = float(input("what's a? "))
    b = float(input("what's b? "))
    print("addition of a and b is", add(a, b))

def add(x, y):
    return x + y

main()