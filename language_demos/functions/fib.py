import itertools

def fibonacci():
    """ generate an infinite fibonacci sequence """

    num_1 = 0
    num_2 = 1

    # returns the first zero in the fibonacci sequence
    yield 0

    # when the next number is requested, the fibonacci method resumes here

    # https://realpython.com/introduction-to-python-generators/#example-2-generating-an-infinite-sequence
    # generates an infinite loop to generate an infinite sequence of
    # fibonacci numbers, but because numbers are only generated when
    # requests, the loop does not run forever, unless fibonacci numbers
    # are requested forever
    while True:

        next_num = num_1 + num_2
        yield next_num
        num_1 = num_2
        num_2 = next_num

# https://docs.python.org/3/library/itertools.html#itertools.islice
# islice enables slicing of values from the generator
for num in itertools.islice(fibonacci(), 0, 10):
    print(num)
