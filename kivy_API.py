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
    When the search button is pressed, the 5 hottest posts on that subreddit are displayed on buttons
    If no posts are found, "No Posts Found" is printed instead
    """

    def get_subreddit_posts(self):
        """
        Sets the text of the buttons to strings containing the titles of the 5 hottest posts
        :return: None
        """
        title_string = ""
        post_list = get_posts(self.ids.subreddit_input.text)
        if post_list is None:
            self.ids.sub_post_1.text = "No Posts Found"
            self.ids.sub_post_2.text = "No Posts Found"
            self.ids.sub_post_3.text = "No Posts Found"
            self.ids.sub_post_4.text = "No Posts Found"
            self.ids.sub_post_5.text = "No Posts Found"
        else:
            self.ids.sub_post_1.text = post_list[0].title
            self.ids.sub_post_2.text = post_list[1].title
            self.ids.sub_post_3.text = post_list[2].title
            self.ids.sub_post_4.text = post_list[3].title
            self.ids.sub_post_5.text = post_list[4].title


class UsernameScreen(Screen):
    """
    The UsernameScreen class extends the Screen class and creates
    a new screen displaying a reddit user's profile.
    """
    def get_userprofile(self):
        """
        get_userprofile() function calls get_redditor_info function to

        :return:
        """
        userprofile = get_redditor_info(self.ids.username_input.text)
        if userprofile is None:
            self.ids.userprofile_output.text = "Error, user not found."
        else:
            self.ids.userprofile_output.text = userprofile


class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("API.kv")


class APIApp(App):
    def build(self):
        return presentation


APIApp().run()
