from app.observer.Observer import Observer


class SpreadSheet(Observer):
    def __init__(self, data_source):
        self.data_source = data_source

    def update(self):
        print("Spreadsheet got notified : {}".format(self.data_source.get_value()))
