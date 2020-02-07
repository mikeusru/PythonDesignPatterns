from app.chainOfResponsibility.Authenticator import Authenticator
from app.chainOfResponsibility.Handler import Handler


class WebServer:
    def __init__(self, handler):
        self.handler = handler

    def handle(self, request):
        self.handler.handle(request)
