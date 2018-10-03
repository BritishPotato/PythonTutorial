def test_var_args(farg, *args):
    print("formal arg", farg)
    for arg in args:
        print("another arg:", arg)
 # 1 formal (positional) argument, later (length) arguments become args SET. NOT LIST

test_var_args(1, "two", 3)

def test_var_kwargs(farg, **kwargs):
    print("formal arg:", farg)
    print(kwargs)
    for key in kwargs:
        print("another keyword arg: %s: %s:" % (key, kwargs[key]))

test_var_kwargs(farg=1, myarg2="two", myarg3=3)
