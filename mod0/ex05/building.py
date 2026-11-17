from sys import argv


# Analyzes the given string and prints out the results
def scan_string(input: str) -> None:
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[]^_`{|}~"
    upper = 0
    lower = 0
    punct = 0
    digits = 0
    spaces = 0
    for char in input:
        upper += char.isupper()
        lower += char.islower()
        digits += char.isdigit()
        spaces += char.isspace()
        punct += char in punctuation
    print(f"The text contains {len(input)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main() -> None:
    """
 Analyzes a given string for types of characters
 Use:
    building.py 'Hello World!'
 Error Checks
    Argument Count == 1"""
    argc = len(argv)
    if (argc < 2):
        return
    if (argc > 2):
        print("AssertionError: Too many arguments given")
        return
    scan_string(argv[1])


if __name__ == "__main__":
    main()
