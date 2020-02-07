from app.chainOfResponsibility.Handler import Handler


class Compressor(Handler):
    def do_handle(self, request):
        print("Compress")
        return False
