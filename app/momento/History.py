class History:
    def __init__(self):
        self.editor_state = []

    def push(self, state):
        self.editor_state.append(state)

    def pop(self):
        return self.editor_state.pop(-1)
