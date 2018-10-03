def f(x): return x**2
print(f(8))

g = lambda x: x**2
print(f(8))

# as you can see they are near identical, only syntatically different

def make_incrementor(n): return lambda x: x + n

f = make_incrementor(2)
g = make_incrementor(6)

print(f(42), g(42))

print(make_incrementor(22)(33))


# this way you can create multiple different incrementor functions and assign them to variables,
# then use them independent from each other. you don't even have to assign the function,
# the code becomes self documenting.

sentence = "It is raining cats and dogs"
words = sentence.split()
print(words)

pairs = [(1, "one"), (2,"two"), (3, "three"), (4, "four")]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

# using lambda to sort list of tuples based on a certain key
# pair[1] --> sorting by the key of the elements in the index position of 1 in each tuple
# "one", "two" etc. pair[0] sorts by number while pair[3] does not exist, (only two sections
# within tuple
