import jsonpickle

from calc_app.history_storage import HistoryStorage

class HistoryFileStorage(HistoryStorage):

    def load(self, history_list):
        with open("history.json", "r") as f:
            history_entry_list = jsonpickle.decode(f.read())
            history_list.replace_history(history_entry_list)

    def save(self, history_list):
        with open("history.json", "w") as f:
            f.write(jsonpickle.encode(list(history_list))) 