# Tutorial on Decorators: https://realpython.com/primer-on-python-decorators/

class App:

    def __init__(self):
        self.__routes = {}

    def route(self, path):
        def wrapper(fn):
            self.__routes[path] = fn
            def inner(*args, **kwargs):
                return fn(*args, **kwargs)
            return inner
        return wrapper

app = App()

@app.route("/")
def do_it(a, b):
    return a + b

# params_wrapped_do_it = app.route("/")(do_it)
