from app.mediator.UIControl import UIControl


class TextBox(UIControl):
    def __init__(self):
        super().__init__()
        self.content = ""

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content
        self._notify_event_handlers()
