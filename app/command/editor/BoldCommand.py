from app.command.editor.UndoableCommand import UndoableCommand


class BoldCommand(UndoableCommand):
    def __init__(self, document, history):
        self.prev_content = None
        self.html_document = document
        self.history = history

    def unexecute(self):
        self.html_document.set_content(self.prev_content)

    def execute(self):
        self.prev_content = self.html_document.get_content()
        self.html_document.make_bold()
        self.history.push(self)