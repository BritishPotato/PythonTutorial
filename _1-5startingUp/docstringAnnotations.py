# docstring

def kek():
    """Do nothing, but document it.

    Seriously, it does fuck all.
    """
    pass

print(kek) # not dis
print(kek.__doc__)

# annotations

def greeting(name: str) -> str:
    return "Hello", name

print(greeting("faggot"))
         

def f(ham: str, eggs: str = "eggs") -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + " and " + eggs

f("spam")
