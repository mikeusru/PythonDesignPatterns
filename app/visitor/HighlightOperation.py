from app.visitor.Operation import Operation


class HighlightOperation(Operation):
    pass


class HighlightHeading(HighlightOperation):
    def apply(self):
        print("hightlight-heading")


class HighlightAnchor(HighlightOperation):
    def apply(self):
        print("highlight-anchor")
