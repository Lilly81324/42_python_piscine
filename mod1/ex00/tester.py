from give_bmi import give_bmi, apply_limit

print("\n === Simple Example === ")
bmi = give_bmi([2.71, 1.15], [165.3, 38.4])
print(bmi)
print(apply_limit(bmi, 26))

print("\n === Bad first argument === ")
bmi = give_bmi("apple", [165.3, 38.4])
print(bmi)
print(apply_limit("apple", 26))

print("\n === Bad second argument === ")
print(give_bmi([2.71, 1.15], 2))
print(apply_limit([0, 1, 2.0], "alphabet"))

print("\n === Mismatching list length === ")
print(give_bmi([2.71, 1.15], [165.3, 38.4, 5]))
