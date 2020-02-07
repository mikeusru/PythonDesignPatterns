from app.chainOfResponsibility.Handler import Handler


class Logger(Handler):
    def do_handle(self, request):
        print("Log")
        return False
