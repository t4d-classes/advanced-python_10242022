person = { "fn": "Bob", "ln": "Smith" }
person_secure = { "ssn": "123-12-1234" }

print({ **person, **person_secure })

for something in person:
    print(person[something])

print(list(person))

print(*person)

# print(**person)