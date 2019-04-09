from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from subreddit import get_posts
from username import get_redditor_info


class MainScreen(Screen):
    pass


class SubredditScreen(Screen):

    """
    Subreddit Screen
    When the search button is pressed, the titles of the 5 hottest posts on that subreddit are displayed
    If no posts are found, "No Posts Found" is printed instead
    """

    def get_subreddit_posts(self):
        """
        Sets the text of the label to a string containing the titles of the 5 hottest posts
        :return: None
        """
        title_string = ""
        post_list = get_posts(self.ids.subreddit_input.text)
        if post_list is None:
            self.ids.sub_output.text = "No Posts Found"
        else:
            for title in post_list:
                title_string += (title.title + '\n')

            self.ids.sub_output.text = title_string


class UsernameScreen(Screen):
    def get_userprofile(self):
        userprofile = get_redditor_info(self.ids.username_input.text)

        self.ids.userprofile_output.text = userprofile


class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("API.kv")


class APIApp(App):
    def build(self):
        return presentation


APIApp().run()
