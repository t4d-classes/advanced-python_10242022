
from webbrowser import get


history = []

math_ops = {
    "add": lambda a,b: a + b,
    "subtract": lambda a,b: a - b,
    "multiply": lambda a,b: a * b,
    "divide": lambda a,b: a / b,
    "exponent": lambda a,b: a ** b
}

def get_command():
    return input("Enter a command:")

def get_operand():
    return float(input("Please enter an operand:"))

def get_history_entry_id():
    return int(input("Enter a history entry id to remove: "))


def get_next_id(history):
    next_id = 1
    if history:
        next_id = max([ entry["id"] for entry in history ]) + 1
    return next_id


def append_history_entry(history, id, opName, opValue):
    history.append({
        "id": id,
        "opName": opName,
        "opValue": opValue
    })

def remove_history_entry(history, entry_id):
    # global history
    # history = [ entry for entry in history if entry["id"] != entry_id ]

    for entry in history:
        if entry["id"] == entry_id:
            history.remove(entry)
            break

def calc_result(history):
    result = 0
    for entry in history:
        result = math_ops[entry["opName"]](result, entry["opValue"])
    return result


def command_calc():
    operand = get_operand()
    append_history_entry(
        history,
        get_next_id(history),
        "add",
        operand)
    print(calc_result(history))

def command_remove_history_entry():
    history_entry_id = get_history_entry_id()
    remove_history_entry(history, history_entry_id)

def command_clear_history():
    global history
    history = []

def command_show_history():
    for entry in history:
        print(entry)

def command_invalid():           
    print("Invalid Command, Try Again.")


while True:

    command = get_command()

    if command in math_ops:
        command_calc()
    elif command == "remove":
        command_remove_history_entry()
    elif command == "clear":
        command_clear_history()
    elif command == "history":
        command_show_history()
    elif command == "exit":
        break
    else:
        command_invalid()


