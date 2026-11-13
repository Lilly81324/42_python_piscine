ft_list = ["Hello"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list.append("World!")
# Tuples are immutable, so they must be reasigned
ft_tuple = ft_tuple[:1] + ("Germany!",)
# Set cant be ord
ft_set.remove("tutu!")
ft_set.add("Wolfsburg!")
ft_dict["Hello"] = "42Wolfsburg!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)