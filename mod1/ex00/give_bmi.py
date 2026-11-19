def bmi_generator(height: list[int | float],
                  weight: list[int | float]):

    """Not safe, calculates and yields result of bmi"""

    maxIndex = min(len(height), len(weight))
    for i in range(maxIndex):
        yield (weight[i] / (height[i] * height[i]))
    return


def check_list(subject: list[int | float]) -> bool:

    """Check if lists contents are really numeric"""

    if not isinstance(subject, list):
        print("Error: List is invalid Type")
        return False
    for entry in subject:
        if not isinstance(entry, int | float):
            print(f"Error: {entry} in list is not a number")
            return False
    return True


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:

    """Creates list of bmi values for given height and weight lists"""

    if not check_list(height) or not check_list(weight):
        return []
    if not len(height) == len(weight):
        print("Error: Weight or length missing entries")
        return []
    return (list(bmi_generator(height, weight)))


def apply_limit(bmi: list[int | float],
                limit: int) -> list[bool]:
    if not check_list(bmi):
        return []
    if not isinstance(limit, int):
        print("Error: Limit value should be integer")
        return []
    results = []
    for value in bmi:
        results.append(value > limit)
    return (results)
