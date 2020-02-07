class StopWatch:

    def __init__(self):
        self.is_running = False
        self.status_name = {
            False: "Not Running",
            True: "Running"
        }

    def click(self):
        self.is_running = not self.is_running
        print(self.status_name[self.is_running])


