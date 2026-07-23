x = float(input("what's x? "))
y = float(input("What's y? "))

print(x+y)

# rounding of output
a = round(x+y, 2)
print(a)
z = round(x+y)
print(z)

# printing number in format 1,000,000 likewise
print(f"{z:,}")

p = float(input("what's p? "))
q = float(input("What's q? "))
r = p/q
print(r)
s = round(p/q , 2)
print(s)
t = p/q
print(f"{t:.2f}")      #using format string

print(0.1+0.2)