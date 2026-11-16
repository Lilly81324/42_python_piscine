from subprocess import run

def test() -> None:
	run(["python", "./mod0/ex07/filterstring.py", "abc de f ghijkl", "a"])
	print("Expected: AssertionError")
	run(["python", "./mod0/ex07/filterstring.py", "abc de f ghijkl", "1", "2"])
	print("Expected: AssertionError")
	run(["python", "./mod0/ex07/filterstring.py", "abc de f ghijkl"])
	print("Expected: AssertionError")
	run(["python", "./mod0/ex07/filterstring.py"])
	print("Expected: AssertionError")
	run(["python", "./mod0/ex07/filterstring.py", "abc de f ghijkl.", "3"])
	print("Expected: AssertionError")
	run(["python", "./mod0/ex07/filterstring.py", "abc de f ghijkl", "2"])
	print("Expected: abc, ghijkl")
	run(["python", "./mod0/ex07/filterstring.py", "abc de f ghijkl", "0"])
	print("Expected: abc de f ghijkl")


if __name__ == "__main__":
	test()