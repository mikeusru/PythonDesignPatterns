from app.observer.Subject import Subject


class DataSource(Subject):

    def __init__(self):
        super().__init__()
        self.value = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
        self.notify_observers()

