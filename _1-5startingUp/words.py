import sys

words = ["cat", "window" , "defenstrate"]
for w in words:
    print(w, len(w))

a = ["Mary", "had", "a", "little", "lamb"]
for i in range(len(a)): # 0 to 4, since length
                        # of list a is 5
    print(i, a[i])  #0 - Mary
                    #1 - had

print(range(10))    #prints literally "range(0, 10)"

# range(x, y) behaves as if it a list but it really isn't.
# it actually is an object which is iterable:
# suitable as a target for functions and constructs that
# expect something from which they an obtain successive
# items.

# the for statement is an iterator. list() creates lists
# from iterables.

# iterate: to perform/repeat an action on each item
# in a set. (go through)


sys.exit

for w in words:
    if len(w) > 6: # which is "defenstrate" in this case
        words.insert(0, w) # inserts "defenstrate"
                           # into first place of words
                           # over and over again





