class UIControl:
    def __init__(self):
        self._event_handlers = []

    def add_event_handler(self, observer):
        self._event_handlers.append(observer)

    def _notify_event_handlers(self):
        for event_handler in self._event_handlers:
            event_handler.handle()
