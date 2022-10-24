
nums = [1,2,3,4,5]

# imperative code - what you want, how to do what you want

# for (int x=0; x<len(nums); x++)
# {
#     print(nums[x])
# }

# count = len(nums)
# counter = 0

# while counter < count:
#     print(nums[counter])
#     counter = counter + 1

# declarative code - what you want

# very pythonic
# for num in nums:
#     print(num)


def double(x):
    print("in double: ", x)
    return x * 2

# more imperative

# double_nums = []


# for num in nums:
#     double_nums.append(double(num))

# print(nums)
# print(double_nums)

# more declarative

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

# code sample 1

count = len(nums)
counter = 0

while counter < count:
    print(nums[counter])
    counter = counter + 1

for num in nums:
    print(num)

# code sample 2

count = 5
counter = 0

while counter < count:
    print(counter)
    counter = counter + 1

# range produces generator and then I iterate over the generator
for counter in range(count):
    print(counter)




