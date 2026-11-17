from subprocess import run


def test() -> None:
    print("Expecting: AssertionErrors")
    run(["python3", "./mod0/ex06/sos.py"])
    run(["python3", "./mod0/ex06/sos.py", "sos", "sas"])
    run(["python3", "./mod0/ex06/sos.py", "s$s"])
    print("===================")
    print("Expecting: ... --- ...")
    run(["python3", "./mod0/ex06/sos.py", "sos"])
    print("Expecting: ... --- ...")
    run(["python3", "./mod0/ex06/sos.py", "sOS"])
    print("Expecting: \n"
          ".... . .-.. .-.. --- / .-- --- .-. .-.. -.. / -- -.-- / -. "
          ".- -- . / .. ... / .. ... .- .- -.-. / .- -. -.. / .. -- / "
          "-... .. -. -.. .. -. --. / .. -")
    run(["python3", "./mod0/ex06/sos.py",
         "Hello world my name is Isaac and im binding it"])


if __name__ == "__main__":
    test()
