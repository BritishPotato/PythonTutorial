def parrot(voltage,state="a stiff",action="voom",type="Norwegian"):
    # last 3 are optional arguments
    print("-- This parrot wouldn't", action, end=" ")
    print("if you put", voltage, "the volts through it.")
    print("--Lovely, plumage, the", type)
    print("--It's", state, "!")

parrot(5)

print("\n")

parrot(3, "kek", "talk")
# as you can see you can override the default argument by adding in
# the parameter.

print("\n")

def cheeseshop(kind, *arguments, **keywords):
    print("--Do you have any", kind, "?")
    print("--I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

def my_function(kek, **kwargs):
    print(str(kwargs), kek)

my_function("test", a=12, b="abc",c="this is a test")
# positional argument: "test"
# keyword argument: a, b, etc.

def concat(*args, sep="/", repeat =1):
    """Concatenates"""
    print(sep.join(args) * repeat)

print("\n")

concat("earth", "mars", "venus")

concat("earth", "mars", "venus", sep=".")

concat("earth", "mars", "venus", sep="!", repeat = 3)

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)

