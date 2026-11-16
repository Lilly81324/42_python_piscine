from subprocess import run

def test() -> None:
	print("Expecting: AssertionErrors")
	run(["python", "./mod0/ex06/sos.py"])
	run(["python", "./mod0/ex06/sos.py", "sos", "sas"])
	run(["python", "./mod0/ex06/sos.py", "s$s"])
	print("===================")
	print("Expecting: ... --- ...")
	run(["python", "./mod0/ex06/sos.py", "sos"])
	print("Expecting: ... --- ...")
	run(["python", "./mod0/ex06/sos.py", "sOS"])
	print("Expecting: \n" \
	".... . .-.. .-.. --- / .-- --- .-. .-.. -.. / -- -.-- / -. " \
	".- -- . / .. ... / .. ... .- .- -.-. / .- -. -.. / .. -- / " \
	"-... .. -. -.. .. -. --. / .. -")
	run(["python", "./mod0/ex06/sos.py", 
	  "Hello world my name is Isaac and im binding it"])


if __name__ == "__main__":
	test()