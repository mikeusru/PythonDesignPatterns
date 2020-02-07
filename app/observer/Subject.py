class Subject:

    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self):
        self._observers.pop(-1)

    def notify_observers(self):
        for observer in self._observers:
            observer.handle()
