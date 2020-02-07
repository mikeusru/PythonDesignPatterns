from app.visitor.AnchorNode import AnchorNode
from app.visitor.HeadingNode import HeadingNode
from app.visitor.HtmlDocument import HtmlDocument


class Main:

    def __init__(self):
        document = HtmlDocument()
        document.add(HeadingNode())
        document.add(AnchorNode())


if __name__ == "__main__":
    Main()
