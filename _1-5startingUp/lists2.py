# 5.5 DICTIONARIES

# also called "associative memories" or "associative arrays", unlike sequences which are
# indexed by a range of numbers, dictionaries are indexed by "keys" which are immutable
# (strings and numbers can always be keys)

# tuples may also be used, though must contain only strings , numberss or tuples.
# if the tuple contains any mutable object (directly or indirectly), IT CANNOT BE USED AS KEY!!!

# lists cannot be used as keys because lists can be modified in place using index assignments,
# slice assignments, or methods like append() and extend()

# BASICALLY dictionaries are unordered set of key: value pairs (keys MUST BE UNIQUE)


tel  = {1 :  "one", 2 : "two", 3 : "three", "zeynep" : "kawaii"}

tel["kawaii"] = "zeynep"

print(tel)

print(list(tel))

print(list(tel.keys()))

print(tel["zeynep"])

# print(sorted(list(tel.keys())))   does not work because strings cannot be sorted with integers

print(1 in tel)

print("zeynep" not in tel)

# OR JUST USE THE BLOODY dict() FUNCTION (CONSTRUCTOR)
print(dict([("sape", 4139), ("guido", 4217), ("jack", 4098)]))

print({x: x**2 for x in (2, 4, 6)})

denizhan = "potato" 
print(denizhan) # <3

# 5.6 LOOPING TECHNIQUES

kek = {"shit" : "cock", "fat" : "cat", "lol" : "lolololo"}

for k, v in kek.items():
    print(k, v)
    
# enumerate to give position index

for i, v in enumerate(["i like", "kek", "did you know?"]):
    print(i, v)
    
# sequences can be paired by zip()

questions = ["name", "sex", "favourite colour"]
answers = ["Victoria", "male", "turquoise"]

for q, a in zip(questions, answers):
    print("What is your {0}? It is {1}.".format(q, a))

for i in reversed(["what", "is", "love", "baby", "don't", "hurt", "me"]):
    print(i)

basket = ["apple", "orange", "kek", "zenci"]
for f in enumerate(sorted(set(basket))):
    print(f)









