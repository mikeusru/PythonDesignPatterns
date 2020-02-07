from app.command.fx.Command import Command


class CompositeCommand(Command):
    def __init__(self):
        self.commands = []

    def add(self, command):
        self.commands.append(command)

    def execute(self):
        for command in self.commands:
            command.execute()
