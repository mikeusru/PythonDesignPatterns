class EventHandler:

    def __init__(self, fun):
        self._update_fun = fun

    def handle(self):
        self._update_fun()
