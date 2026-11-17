from ft_filter import ft_filter

tests = [[lambda x: x % 2 == 0, range(10)],
         [lambda x: x % 3 == 0, range(10)],
         [lambda x: x == "duck", ["duck", "goose", "duck", "chinken"]],
         [lambda x: x == "dog", ["duck", "goose", "duck", "chinken"]]]

for case in tests:
    goal = list(filter(case[0], case[1]))
    produced = list(ft_filter(case[0], case[1]))
    if (goal == produced):
        print(f"{goal} == {produced}")
    else:
        print(f"Warning! {goal} and {produced} differ!")
print("==================")
print(filter.__doc__)
print("==================")
print(ft_filter.__doc__)
