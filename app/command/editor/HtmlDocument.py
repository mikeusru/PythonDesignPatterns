class HtmlDocument:
    def __init__(self):
        self.content = ""

    def make_bold(self):
        self.content = "<b>{}</b>".format(self.content)

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content