from app.template.Task import Task


class TransferMoneyTask(Task):

    def _do_execute(self):
        print("Transfer Money Done")
