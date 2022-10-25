

# results in an infinite loop
while True:

    first_name = input("please enter your first name: ")

    if not first_name:
        break # exit the loop

    last_name = input("please enter your last name: ")

    if last_name == 'Smith':
        continue # exit this iteration of the loop, but keep looping

    print(first_name)