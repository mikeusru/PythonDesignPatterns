from app.mediator.UIControl import UIControl


class ListBox(UIControl):
    def __init__(self):
        super().__init__()
        self._selection = ""

    def get_selection(self):
        return self._selection

    def set_selection(self, selection):
        self._selection = selection
        self._notify_event_handlers()
