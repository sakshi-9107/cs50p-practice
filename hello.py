print("hello")
print()
str=input("enter your name: \n")
int=input("enter your age: ")
year=input("Year: ")
print(str)
print(int)
print(year)
print()

name = input("what is your name? ")
def greet(name):
    print(f"Hello, {name}!")
    print(f"{name}")
    
greet("world")
greet("sakshi")
print(f"hello, {name}")


nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # [1, 4, 9, 16]






text = input()
print(text.replace(" ", "..."))