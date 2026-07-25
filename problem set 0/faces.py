# In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.
def main():
    text = input()
    print(convert(text))

def convert(n):
    n = n.replace(":)" , "🙂")
    n = n.replace(":(" , "🙁")
    return n

main()