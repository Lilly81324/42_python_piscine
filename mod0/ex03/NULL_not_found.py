from typing import Any


def NULL_not_found(object: Any) -> int:
    # cant check for nan unless you check against itself
    if not object or (object != object):
        # no NoneType, so test for value
        dict = {float: "Cheese", int: "Zero", str: "Empty", bool: "Fake"}
        if object is None:
            varname = "Nothing"
        else:
            varname = dict[type(object)]
        print(f"{varname}: {object} {type(object)}")
        return (0)
    else:
        print("Type not Found")
        return (1)
