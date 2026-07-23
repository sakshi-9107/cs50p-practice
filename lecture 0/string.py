# asking user for branch name
branch = input("What is your branch name? ")

# remove whitespace from user's input
branch = branch.strip()

# capitalize user's input
# either use capitalize() or title() most of the time prefer "title()"
branch = branch.capitalize()        #capitalize only 1st letter of 1st word
branch = branch.title()        #capitalize 1st letter of each word

# reducing lines
# student name
name = input("Enter your full name ")
name = name.strip().title()

# reducing lines
# college name
clg = input("Enter college name ").strip().title()

# print branch 
print(f"Welcome to {branch} Branch")
# print name
print(f"hello, {name}")
# print clg name
print(f"{clg}")

# spliting user's input 
address = input("Enter city & pincode ")
city, pincode = address.split()
print(f"{address}")
print(f"{city}")
print(f"{pincode}")
