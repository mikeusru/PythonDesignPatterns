from app.mediator.UIControl import UIControl


class Button(UIControl):
    def __init__(self):
        super().__init__()
        self.is_enabled = False

    def get_enabled(self):
        return self.is_enabled

    def set_enabled(self, is_enabled):
        self.is_enabled = is_enabled
        self._notify_event_handlers()
