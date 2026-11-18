from ft_filter import ft_filter

def exceptCheck(func, lst):
    try:
        print(list(filter(func, lst)))
    except (TypeError):
        print(f"{TypeError} == ", end="")
    try:
        print(list(ft_filter(func, lst)))
    except (TypeError):
        print(TypeError)

tests = [[lambda x: x % 2 == 0, range(10)],
         [lambda x: x % 3 == 0, range(10)],
         [lambda x: x == "duck", ["duck", "goose", "duck", "chinken"]],
         [lambda x: x == "dog", ["duck", "goose", "duck", "chinken"]]]

exceptTest = [[1, ["duck"]],
              ["duck", ["duck"]],
              [lambda x: x == "duck", 1],
              [lambda x: x == "duck", "duck"]]

# Test normal cases
for case in tests:
    goal = list(filter(case[0], case[1]))
    produced = list(ft_filter(case[0], case[1]))
    if (goal == produced):
        print(f"{goal} == {produced}")
    else:
        print(f"Warning! {goal} and {produced} differ!")

# Throw typeError if function or list are invalid Type
for case in exceptTest:
    exceptCheck(case[0], case[1])

# If function is None, should yield only true array elements
print(f"{list(filter(None, [0, 1, 2, "", None]))} == ", end ="")
print(list(ft_filter(None, [0, 1, 2, "", None])))

print("==================")
print(filter.__doc__)
print("==================")
print(ft_filter.__doc__)
