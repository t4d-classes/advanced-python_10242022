


while True:

    first_name = input("please enter your first name: ")

    if not first_name:
        break

    last_name = input("please enter your last name: ")

    if last_name == 'Smith':
        continue

    print(first_name)