class Handler:
    def __init__(self, next_handler):
        self.next_handler = next_handler

    def handle(self, request):
        if self.do_handle(request):
            return
        if self.next_handler:
            self.next_handler.handle(request)

    def do_handle(self, request):
        raise NotImplementedError
