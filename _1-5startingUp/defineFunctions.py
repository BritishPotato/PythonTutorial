# let's create functions and shit!

def fib(n): # fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()

# let's try it out
fib(20000000000000000000000000000000000000000000000000000000000000)

print(fib)

def fib2(n): # return fibonacci series up to n
    """Return a list containing the Fibonacci series up to n"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        # calls a method of the list object result.
        # a method is a function that belongs to an object
        # and is named obj.methodname
        # (it is possible to define your own object types
        # and methods using classes.

        # append() is a method defined for list objects,
        # it adds a new element at the end of the list.
        # append() is equivalent to result = result + [a]
        # but more efficient.

def ask_ok(prompt, retries=4, remind="Please try again"):
    "Asks for y/n prompt, 4 tries available"""
    while True:
        ok = input(prompt + "\n")
        if ok.lower() in ("y", "ye", "yes"):
        # in: tests whether or not a sequence has a certain val
            print("You have said yes.")
            return True
        if ok.lower() in ("n", "no", "nop", "nope"):
            print("You have said no.")
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError("invalid user response")
        print(reminder)
        
# ask_ok(kek) does not work because it must manually be a string

ask_ok("Would you liek to?")

i = 5

def f(arg=1):
    print(arg)

i = 6

# PRINTS 5, NOT 6! THE DFAULT VALUE IS EVALUATE ONLY ONCE.

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# prints
# [1]
# [1, 2]
# [1, 2, 3]  --> This accumulates, does not reset!!!

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# prints
# [1]
# [2]
# [3] --> as you can see default no longer shared










        
