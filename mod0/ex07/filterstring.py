from sys import argv


def main() -> None:
    """
 Prints all the given words that are longer then a given number
 Use:
     filterstring.py 'Hello the World' 4
 Errorchecks:
     Arg Count == 2
     First Args chars must be aphanumeric or space
     Second Arg must be num"""
    if (len(argv) != 3):
        print("AssertionError: the arguments are bad")
        return
    try:
        minLength = int(argv[2])
    except (ValueError):
        print("AssertionError: the arguments are bad")
        return
    for char in argv[1]:
        if not char.isalnum() and not char == ' ':
            print("AssertionError: the arguments are bad")
            return

    # make list of tokens
    tokens = argv[1].split(" ")

    # for each token print
    result = list(filter(lambda word: len(word) > minLength, tokens))
    print(result)


if __name__ == "__main__":
    main()
