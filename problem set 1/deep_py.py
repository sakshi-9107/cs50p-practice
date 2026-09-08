def main():
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    normalized = answer.strip().lower()

    if normalized in ("42", "forty-two", "forty two"):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
