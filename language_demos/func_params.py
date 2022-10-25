

nums = [1,2,3, { "name": "Bob" },5]


def add_six_to_list(some_list):
    some_list.append(6)
    # some_list = [1,2,3,4,5,6]


print(nums)

add_six_to_list(nums)

print(nums) # output: [1,2,3,4,5,6]