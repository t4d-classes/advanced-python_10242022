from calc_app.user_input import (
    get_operand, get_history_entry_id
)
from calc_app.history import (
    get_next_id, append_history_entry,
    remove_history_entry, calc_result
)

from calc_app.math_ops import math_ops

def command_calc(history, op_name):
    operand = get_operand()
    append_history_entry(
        history,
        get_next_id(history),
        op_name,
        operand)
    print(calc_result(history, math_ops))

def command_remove_history_entry(history):
    history_entry_id = get_history_entry_id()
    remove_history_entry(history, history_entry_id)

def command_clear_history():
    return []

def command_show_history(history):
    for entry in history:
        print(entry)

def command_invalid():           
    print("Invalid Command, Try Again.")
