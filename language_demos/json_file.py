import jsonpickle # https://jsonpickle.github.io/

# JSON Pickle is used to serialize custom classes to JSON because Python's
# build-in JSON serializer cannot serialize custom objects

class Color:

    def __init__(self, name, hexcode):
        self.name = name
        self.hexcode = hexcode

    def __repr__(self):
        return f"name: {self.name}, hexcode: {self.hexcode}"

colors = [
    Color("red", "ff0000"),
    Color("green", "00ff00"),
    Color("blue", "0000ff"),
]

# unpicklable - True if the JSON can be deserialized into Python objects of
# a certain class, and False if the JSON should not be deserialized into
# Python objects of a certain class
print(jsonpickle.encode(colors, unpicklable=False))

# Encode a JSON string from a Python object and write it to a file
# "w" - opens the file in write mode overwriting the original file
with open("colors.json", "w") as f:
    f.write(jsonpickle.encode(colors))


# "r" - opens the file in read mode
with open("colors.json", "r") as f:
    json_string = f.read()
    colors2 = jsonpickle.decode(json_string)

    for color in colors2:
        print(color)
