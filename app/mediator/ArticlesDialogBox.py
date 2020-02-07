from app.mediator.Button import Button
from app.mediator.ListBox import ListBox
from app.mediator.EventHandler import EventHandler
from app.mediator.TextBox import TextBox


class ArticlesDialogBox:
    def __init__(self):
        self.articles_list_box = ListBox()
        self.title_text_box = TextBox()
        self.save_button = Button()
        self.articles_list_box.add_event_handler(EventHandler(self.article_selected))
        self.title_text_box.add_event_handler(EventHandler(self.title_changed))

    def title_changed(self):
        content = self.title_text_box.get_content()
        is_empty = not content
        self.save_button.set_enabled(not is_empty)

    def article_selected(self):
        self.title_text_box.set_content(self.articles_list_box.get_selection())
        self.save_button.set_enabled(True)

    def simulate_user_interaction(self):
        self.articles_list_box.set_selection("Article 1")
        # self.title_text_box.set_content("")
        # self.title_text_box.set_content("Article 2")
        print("Text Box: {}".format(self.title_text_box.get_content()))
        print("Button: {}".format(self.save_button.get_enabled()))

