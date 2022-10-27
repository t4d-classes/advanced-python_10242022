
# https://towardsdatascience.com/basics-of-python-generators-a47b3cab1a23


def do_it():

    print("do it 1")
    # yield is used instead of return because Python will resume
    # execution on the next line of code when the next value is
    # requested from the generator
    yield 1 
    print("do it 2")
    yield 2
    print("do it 3")
    yield 3

# generator objects are iterable, and generate a new value each time it
# is requested by the for-in loop, if no more values can be generated the
# loop exits
for num in do_it():
    print("for ", num)
