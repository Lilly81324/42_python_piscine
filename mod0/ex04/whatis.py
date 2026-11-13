from sys import argv


def checkArgs() -> None:
    argc = len(argv)
    if (argc < 2):
        return
    if (argc > 2):
        print("AssertionError: more than one argument is provided")
        return
    try:
        num = int(argv[1])
        if (num % 2 == 0):
            print("I'm Even")
        else:
            print("I'm Odd")
    except (ValueError):
        print("AssertionError: argument is not an integer")
        return


checkArgs()
