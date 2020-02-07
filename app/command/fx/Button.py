

class Button:
    def __init__(self, command):
        self.label = ""
        self.command = command

    def click(self):
        self.command.execute()

    def get_label(self):
        return self.label

    def set_label(self, label):
        self.label = label

