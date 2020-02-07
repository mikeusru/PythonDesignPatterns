from queue import Queue


class History:
    def __init__(self):
        self.commands = Queue()

    def push(self, command):
        self.commands.put(command)

    def pop(self):
        return self.commands.get()

    def empty(self):
        return self.commands.empty()