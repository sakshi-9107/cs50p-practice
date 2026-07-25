# In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
m = int(input("mass (m) in kg = "))
c = 300000000
E = m * (pow(c , 2))        # m*(c**2) / m*(c*c)
print("E=", E)
