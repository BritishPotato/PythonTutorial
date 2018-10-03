x = {1, 2 ,3} # set
x = [1, 2, 3] # list
print(x)

x.append(4)
# adds item at end of list
print(x)

x.extend(["a", "b", "b", "c"])
# add iterable (list to go through)
print(x)

x.insert(2, "inside we go")
# inside we go
print(x)

x.pop(1)
# x.pop([1, 2]) for multi index
# x.pop() for last item go pop
# and pop it goes
print(x)

y=x.copy() # NOT Y = X BECAUSE IT STILL CLEARS X
y.clear()
# pop it ALL goes
print(y)

print(x)
print(x.index("a"))

print(x.count("b"))

print(x.reverse()) # returns None because reverse() modifies list in place BUT RETURNS NONE
# HOWEVER IT STILL DOES THE REVERSAL, CHANGING THE ORIGINAL LIST 
# x = x.reverse() nope not this either because this time x is defined as None 
#x.reverse() # DOES NOT WORK? CHECK LATER
print(x)
x.reverse() # to show that below code also works
print(x[::-1])
print(x) # x is still original though

# for lists, while append and pop is quick for the end of a list, it is slow for the beginning of a list,
# because all other elements must be shifted by one

# to implement a queue use collections.deque, which is designed for fast append and pops at
# both ends

# 5.1.2 USING LISTS AS QUEUES

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft() # bye Eric (first comer)!
queue.popleft() # bye John (second comer)!
print(queue)
from collections import deque

# 5.1.3 LIST COMPREHENSIONS

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
print(x)
# x is created and still exists after loop completed.
x = None

squares = list(map(lambda x: x**2, range(10)))
# or
squares = [x**2 for x in range(10)]
# is more concise and readable, x does not exit outside of function

print(squares)
print(x)

k = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# this listcomp combines the elements of two lists if they are not equal
# it is equivalent to:
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print(k)
print(combs)

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
print([x*2 for x in vec])

# no negative
print([x for x in vec if x>0])

# function to all elements
print([abs(x) for x in vec])

# method to all elements
nom = ["  1       ", "2       ", "     3 "]
print([kek.replace(" ", "lol") for kek in nom])

# can create 2 or 3-tuples
print([(x, x*2, x**2) for x in range(10)])

from math import pi
print([str(round(pi, i)) for i in range(1,10)])

#  5.1.4 NESTED LIST COMPRHENSIONS

matrix = [
    [1 ,2 ,3 ,4], [5, 6, 7, 8], [9, 10, 11, 12],
    ]

# print([row[i] for row in matrix])
print([[row[i] for row in matrix] for i in range(4)])

# 5.2 THE DEL STATEMENT

# pop() returns a value. del does not.

a = [-1, 1, 66.25, 33, 33, 1234.5]
print(a)
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
del a
# a no longer exists print(a) gives error.

# 5.3 TUPLES AND SEQUENCES

t = 12345, 54321, "hello!"
print(t)
print(t[0]) # the first

# tuples can also be nested!

u = t, (1, 2, 3, 4, 5)
print(u)

# tuples are immutable (trying to assign causes error)
# t[0] = 8888 for e.g.
# but can contain mutable objects e.g. lists
v = ([1, 2, 3], [3, 2, 1])
print(v)

# empty tuple
empty = ()

# 1 item tuple (note that it requires a comma in the end)
singleton = "this is one item",

print(len(empty))
print(len(singleton))

# tuple packing, for e.g:
t = 12345, 54321, "this is one item"

# sequence unpacking
x, y, z = t

# 5.4 SETS

# unordered collection with no duplicate elements
# use is for membership testing (WHAT?) and destroy duplicates
# supports math operations (like union, intersection, difference, and symmetric difference)

# empty set:
x = set()
# empty dictionary:
x = {} # (will be discussed in next section)

basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
print(basket) # we see duplicates are kill
print("orange" in basket) # gotta go fast membership testing
print("crabgrass" in basket)

# operations on unique letters from two words

a = set("abracadabra")
b = set("alacazam")
print(a)        # unique letters in a
print(a-b)     # letters in a but not in b
print(a|b)    # letters in either a or b
print(a&b)  # letters in both a and b
print(a^b)   # letters in a or b but not both


# set comprehensions are also supported (just like list comprehensions)
a = {x for x in "abracadabra" if x not in "abc"}
# letters which are not a, b or c are stored
print(a)
