
nums = [1,2,3,4,5]

######################################################################

# Iterating over a List

# imperative code - what and how

# For Loop Example - not valid Python code
# for (int x=0; x<len(nums); x++)
# {
#     print(nums[x])
# }

# While Loop Example - valid Python but not Pythonic
# count = len(nums)
# counter = 0

# while counter < count:
#     print(nums[counter])
#     counter = counter + 1


# declarative code - what-only

# very pythonic
# for num in nums:
#     print(num)


######################################################################

# Produce a new List of Transformed Items


def double(x):
    print("in double: ", x)
    return x * 2

# More Imperative

# double_nums = []

# for num in nums:
#     double_nums.append(double(num))

# print(nums)
# print(double_nums)

# More Declarative

#double_nums_gen = map(double, nums) # map generator
#double_nums = list(map(double, nums)) # generate was forced to enumerate to a list

# list comprehension (no generator)
# double_nums = [ double(num) for num in nums ]

# generator comprehension
# double_nums = ( double(num) for num in nums )

# print(double_nums)

# for double_num in double_nums:
#     print("in for loop: ", double_num)

# double_nums = list(double_nums_gen)

# print(double_nums)

#############################################################

# Iterating without and Underlying Data Source

# code sample 1 - with a data source

count = len(nums)
counter = 0

while counter < count:
    print(nums[counter])
    counter = counter + 1

for num in nums:
    print(num)

# code sample 2 - without a data source 

count = 5
counter = 0

while counter < count:
    print(counter)
    counter = counter + 1


# Pythonic way of iterating without a data source
# range produces generator and then I iterate over the generator
for counter in range(count):
    print(counter)




