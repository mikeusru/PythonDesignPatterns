from app.command.editor.Command import Command


class UndoableCommand(Command):
    def __init__(self, history):
        self.history = history

    def execute(self):
        if not self.history.empty():
            self.history.pop().unexecute()