

nums = [1,2,3,4]
# print(nums) # == print([1,2,3,4])
# print(*nums) # == print(1,2,3,4)  // the * unpacks the list into individual arguments


letters = ['a','b','c','d']
# print(letters)

# * is the unpacking operator when used in the expression position
# print(*letters)


# for letter in letters:
#     print(letter)

# * is packing operator when it is used in the variable position
# a,b,*c = nums

# print(a,b,c)

# variable that is assigned the result of an expression
# name = "Bob"

# def do_it(*args):
#     print(param)


# do_it(*[1,2,4])

nums1 = list(range(5))
nums2 = list(range(5))

# print([ *nums1, *nums2  ])

first, *middle, last = [ *nums1, *nums2  ]

print(first, middle, last)