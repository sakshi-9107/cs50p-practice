name = input("what's your name? ")

# if, elif, else statements 
# case 1: 
if name == "Harry":
    print("Griffindor")
elif name == "Hermione":
    print("Griffindor")
elif name == "Ron":
    print("Griffindor")
elif name == "Draco":
    print("Slytherin")
else :
    print("who? ")

# case 2: use of "or" = T or F or F = True
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Griffindor")
elif name == "Draco":
    print("Slytherin")
else :
    print("who? ")


# using "match"
# case 1:
match name:
    case "harry":
        print("griffindor")
    case "hermione":
        print("griffindor")
    case "ron":
        print("griffindor")
    case "draco":
        print("slytherin")
    case _:
        print("who? ")

# case 2:
match name:
    case "HARRY" | "HERMIONE" | "RON":
        print("GRIFFINDOR")
    case "DRACO":
            print("SLYTHERIN")
    case _:
        print("WHO? ")