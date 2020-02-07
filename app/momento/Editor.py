from app.momento.EditorState import EditorState


class Editor:
    def __init__(self):
        self.content = None

    def set_content(self, content):
        self.content = content

    def get_content(self):
        return self.content

    def create_state(self):
        return EditorState(self.content)

    def restore(self, state):
        self.content = state.get_content()
