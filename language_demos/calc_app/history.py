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
    for entry in history:
        if entry["id"] == entry_id:
            history.remove(entry)
            break

def calc_result(history, math_ops):
    result = 0
    for entry in history:
        result = math_ops[entry["opName"]](result, entry["opValue"])
    return result
