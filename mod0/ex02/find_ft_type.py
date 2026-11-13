from typing import Any


def all_thing_is_obj(object: Any) -> int:
    if type(object) is list:
        print("List : ", end="")
    elif type(object) is tuple:
        print("Tuple : ", end="")
    elif type(object) is set:
        print("Set : ", end="")
    elif type(object) is dict:
        print("Dict : ", end="")
    elif type(object) is str:
        print(object, end="")
        print("is in the kitchen: ", end="")
    else:
        print("Type not found")
        return (42)
    print(type(object))
    return (42)
