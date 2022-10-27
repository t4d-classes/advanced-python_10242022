
# # defining the function
# def do_it():
#     print("did it")


# # invoking the function
# # do_it()

# def get_one():
#     return "1"

# def call_me(something):
#     print(something) # ?


# call_me(get_one) # function object ref
# call_me(get_one()) # 1




# call_me(do_it)

# this_is_cool = do_it

# this_is_cool()


# num_1 = 2

# def add(x,y):
#     return x + y


# the_sum = add(num_1,2 + 3)


def outer(x):

    def inner():
        print(x) # x is a closure
    
    return inner


cool = outer(4)

cool()

def do_it(fn):
    print(fn(1,2))

# correct use of lambda
do_it(lambda x,y: x + y)

# lambda anti-pattern, use def
cool = lambda x,y: x + y

cool(1,2)