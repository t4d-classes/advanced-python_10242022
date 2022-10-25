from calc_app.user_input import (
    get_command
)

from calc_app import commands
from calc_app.math_ops import is_math_op

def app():

    history = []

    while True:

        command = get_command()

        if is_math_op(command):
            commands.command_calc(history, command)
        elif command == "remove":
            commands.command_remove_history_entry(history)
        elif command == "clear":
            history = commands.command_clear_history()
        elif command == "history":
            commands.command_show_history(history)
        elif command == "exit":
            break
        else:
            commands.command_invalid()

if __name__ == "__main__":
    app()


