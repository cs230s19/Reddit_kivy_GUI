from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from subreddit import get_posts


class MainScreen(Screen):
    pass




class SubredditScreen(Screen):
    "takes whatever text is currently on the screen then goves it to the "

    def get_subreddit_posts(self):
        title_string = ""
        dict = get_posts(self.ids.subreddit_input.text)
        if dict is None:
            self.ids.sub_output.text = "No Posts Found"
        else:
            for title in dict:
                title_string += (title.title + '\n')

            self.ids.sub_output.text = title_string



class UsernameScreen(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("API.kv")


class APIApp(App):
    def build(self):
        return presentation


APIApp().run()
