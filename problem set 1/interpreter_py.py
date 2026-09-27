def main():
    x, y, z = input("Expression: ").split()
    print(calculate(x, y, z))


def calculate(x, y, z):
    x = int(x)
    z = int(z)

    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z
    else:
        raise ValueError("Invalid operator")

    return f"{result:.1f}"


if __name__ == "__main__":
    main()
