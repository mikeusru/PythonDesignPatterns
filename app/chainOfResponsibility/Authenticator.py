from app.chainOfResponsibility.Handler import Handler


class Authenticator(Handler):

    def do_handle(self, request):
        is_valid = request.username == "admin" and \
                   request.password == "1234"
        print("Authentication")
        return not is_valid
