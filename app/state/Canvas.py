from app.state.Tool import Tool


class Canvas:

    def __init__(self):
        self.current_tool = Tool()

    def set_current_tool(self, tool):
        self.current_tool = tool

    def mouse_down(self):
        self.current_tool.mouse_down()

    def mouse_up(self):
        self.current_tool.mouse_up()