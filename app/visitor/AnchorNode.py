from app.visitor.HtmlNode import HtmlNode


class AnchorNode(HtmlNode):
    def excecute(self, operation):
        operation.apply(self)

