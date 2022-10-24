

def do_it():

    print("do it 1")
    yield 1
    print("do it 2")
    yield 2
    print("do it 3")
    yield 3


for num in do_it():
    print("for ", num)
