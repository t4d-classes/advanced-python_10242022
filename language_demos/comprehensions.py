

# [ ] - list comprehension
print([ x * 2 for x in range(10) ])

# ( ) - generator comprehension
print(( x * 2 for x in range(10) ))

# { : } - dictionary comprehension
print({ x: x * 2 for x in range(10) })

# { } - set comprehension
print({ x * 0 for x in range(10) })
