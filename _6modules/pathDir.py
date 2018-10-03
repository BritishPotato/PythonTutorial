import sys, fibo

# interpreter's search path for modules
print(sys.path) 

print("\n")

# names the module fibo defines
print(dir(fibo))

print("\n")

# names the module sys defines
print(dir(sys))

print("\n")

a = [1, 2, 3]

# names the names currently defined
print(dir())
# as you can see it lists all types of names: variables, modules, functions, etc.

print("\n")

# however it does not list the names of built-in functions and variables
# u need to important builtins fo dat

import builtins

print(dir(builtins))
