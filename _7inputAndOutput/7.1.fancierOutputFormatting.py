#str()     --> representations of values which are human-readable
#repr()  --> representations whixh can be read by the interpreter (force SyntaxError if no syntax)

s = "Hello, world."
print(str(s))    #--> Hello, world.
print(repr(s)) #--> 'Hello, world.'

print(str(1/7))

x = 10 * 3.25
y = 200 * 200

s = "The value of x is " +  repr(x) + ", and y is " + repr(y) + "...   " + str(x)+" "+str(y) 
print(s)

# the repr() of a string adds string quotes and backslashes:
hello = "hello, world\n"
print(hello)
hellos = repr(hello) # THIS ALLOWS FOR \N AND " " TO ALSO BE SEEN!!!!
print(hellos)

# the argument to repr() may be any Python object:
print(repr((x,y,("spam", "eggs"))))


# TABLE OF SQUARE AND CUBES
for x in range(1, 11):
    print(repr(x).rjust(2), " *", repr(x*x).rjust(3), end=" = ") # rjust kaydırıyor
    # use of "end" on previous line
    print(repr(x*x*x).rjust(4))

for x in range(1, 11):
    print("{0:2d} * {1:3d} = {2:4d}".format(x, x*x, x*x*x))

# this demonstrate the str.rjust() method of string objects
# it right-justifies a string by padding it with spaces on the left

y = "kek"

print(y.center(10, "a"))
print(y.rjust(10,"a"))
print(y.ljust(10,"a"))

for x in range(1,11):
    for y in range(101, 111): 
        print(x, "is first", y, "is second")
# stays in 1, y=101, 102, 103...
# then stays in 2, y=101, 102, 103...

# str.format() method looks like this:
bob = "6thisIsAString78"
print(bob.zfill(10))
print("We are the {1} who say {0}!".format("knights", "Ni"))

print("This {food} is {adjective}.".format(food="spam", adjective="horrible"))

contents = "kek"
print("I want some {}".format(contents))
# !a applies ascii(), !s applies str(), !r applies repr()
print("I want some {!r}".format(contents))

# ":" allows greater control over how the value is formatted.
# for example, this example rounds Pi to three places after the decimal
import math
print("The value of PI is approximately {0:.3f}.".format(math.pi))

# integer after the ":" will cause that field to be a minimum number of characters wide
# useful for making tables kawaii
table = {"Sjoerd":4127, "Jack":4098, "Dcab":7678}
for name, phone in table.items():
    print("{0:10} ==> {1:10d}".format(name, phone))

# if you have long format string but don't want to split it up, simply passing the dict and
# using square brackets "[]" to access the keys is possible.
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d};' 'Dcab: {0[Dcab]:d}'.format(table))

# can also be done by passing the table as keyword arguments with the ** notation
print("Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}".format(**table))
# useful in combination with the built-in function vars() which returns a dictionary
# containing all local variables

import math

print("The value of PI is approximately %5.5f." % math.pi)



print("zeynep is still here") #kehkehkeh
print("Zeynep was here")
print("sprint")
