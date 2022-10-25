import jsonpickle

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

print(jsonpickle.encode(colors, unpicklable=False))

with open("colors.json", "w") as f:
    f.write(jsonpickle.encode(colors))

with open("colors.json", "r") as f:
    json_string = f.read()
    colors2 = jsonpickle.decode(json_string)

    for color in colors2:
        print(color)
