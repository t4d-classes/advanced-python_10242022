from calc_app.user_input import get_command
from calc_app.history_list import HistoryList
from calc_app.calculator import Calculator

def app():

    history_list = HistoryList()
    calculator = Calculator(history_list)

    while True:

        command = get_command()

        if calculator.is_math_op(command):
            calculator.command_calc(command)
        elif command == "remove":
            calculator.command_remove_history_entry()
        elif command == "clear":
            calculator.command_clear_history()
        elif command == "history":
            calculator.command_show_history()
        elif command == "exit":
            break
        else:
            calculator.command_invalid()

if __name__ == "__main__":
    app()


