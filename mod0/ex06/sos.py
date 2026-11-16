from sys import argv


def main() -> None:
    """
 Converts the first given argument into morse code
 Use:
    sos.py 'Sos'
 Errorchecks:
    Argument count == 1
    
    """
    argc = len(argv)
    if (argc != 2):
        print("AssertionError: the arguments are bad")
        return
    for char in argv[1]:
        if not char.isalnum() and not " ":
            print("AssertionError: the arguments are bad")
            return
    NESTED_MRSE = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "=": "-...-"}
    firstchar = 1
    for char in argv[1].upper():
        if not firstchar:
            print(" ", end="")
        else:
            firstchar = 0
        print(NESTED_MRSE[char], end="")
    print("")


if __name__ == "__main__":
    main()
