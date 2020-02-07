from app.command.fx.Command import Command


class AddCustomerCommand(Command):
    def __init__(self, service):
        self.service = service

    def execute(self):
        self.service.add_customer()