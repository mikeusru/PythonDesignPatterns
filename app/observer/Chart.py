from app.observer.Observer import Observer


class Chart(Observer):
    def __init__(self, data_source):
        self.data_source = data_source

    def update(self):
        print("Chart got updated: {}".format(self.data_source.get_value()))

