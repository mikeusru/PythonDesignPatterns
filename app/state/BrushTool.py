from app.state.Tool import Tool


class BrushTool(Tool):
    def mouse_down(self):
        print("Brush Icon")

    def mouse_up(self):
        print("Draw a line")