from numpy import array

def slice_me(family: list, start: int, end: int) -> list:

    """Slices 2d array into less arrays"""

    # Type check
    if not isinstance(family, list) or \
        not isinstance(start, int) or \
        not isinstance(end, int):
        print("Error: Invalid Type given")
        return []
    for member in family:
        if not isinstance(member, list):
            print("Error: Part of the array is not another array")
            return []
        if (len(member) != len(family[0])):
            print(f"Error: Not all sub-arrays are the same size")
            return []
    # vulnerable to subarrays being different sizes
    famArray = array(family)
    dimensions = famArray.shape
    if (len(dimensions) != 2):
        print(f"Error: Invalid Dimension Count of {len(dimensions)}, must be 2")
        return []
    print(f"My shape is: ({famArray.shape[0]}, {famArray.shape[1]})")
    return (famArray[start:end])
    #your code here

family = [[1.80, 5],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))