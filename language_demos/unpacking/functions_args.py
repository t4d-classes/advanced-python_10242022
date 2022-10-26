

# def add(x,y,z=2,a=-1):
#     return x + y + z + a


# nums = [1,2,3,4]

# print(add(1,2,3,4))
# print(add(*nums))

# nums2 = [1,2]
# some_args = { "z": 10, "a": 3 }

# print(add(*nums2, **some_args))


# def mul(*args):
#     result = args[0]
#     for arg in args[1:]:
#         result = result * arg
#     return result

# from functools import reduce

# def mul2(*args):
#     return reduce(lambda a,b: a*b, args)

# nums = [4,1,9,2,3,7]

# print(mul(*nums))
# print(mul2(*nums))

# #    a, b
# #    4, 1
# #    4, 9
# #   36, 2
# #   72, 3
# #  216, 7
# # result: 1512

# def do_it(**kwargs):
#     print(kwargs)

# do_it(a=2,b=4,c=6,d=7,e=8)


# do not recommend using the globals and locals function

# outside = "test"

# def some_fn(param1):

#     outside = ['this', 'is', 'not', 'a', 'good', 'idea']
#     inside = 2
#     print(globals()["outside"], inside, param1, outside)

#     print(globals())
#     print(locals())

# some_fn(True)



var t # declaration

t = 3 # assignment

var t = 3 # combined declaration and assignment

fn do_it() {
   #global t
    t = 4

    print(t)


}

do_it()
print(t) -> 3