def count_in_list(list, word) -> int:
    """Returns amount of times the given word appears in the given list"""
    counter = 0
    for words in list:
        if words == word:
            counter += 1
    return (int(counter))
