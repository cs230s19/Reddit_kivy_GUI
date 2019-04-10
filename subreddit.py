import praw
from prawcore import exceptions

"""reddit object uses account to get access to Reddit api"""
reddit = praw.Reddit(client_id='bFbCvelvrdVuFA',
                     client_secret='HjJOdVpi_jERV4T8PhAmxwtEM6w',
                     password='CaramelApple',
                     user_agent='testscript by /u/CS230_throwaway',
                     username='CS230_throwaway')


def get_posts(subreddit_name):
    """
    Gets the top 5 hottest posts from given subreddit not including stidkied posts

    :param subreddit_name: String from InputText containing name of subreddit
    :return: If posts are found: A list of submissions representing the posts
            If no posts are found: None is returned
    """
    num_stickied = 0
    num_posts = 10
    post_list = []

    if subreddit_name == "":
        return None

    hot_posts = reddit.subreddit(subreddit_name).hot(limit=num_posts)

    try:
        for x in hot_posts:
            if x.stickied:
                num_stickied += 1
    except exceptions.Redirect:
        return None

    dict = reddit.subreddit(subreddit_name).hot(limit=num_posts + num_stickied)
    for x in dict:
        if not x.stickied:
            post_list.append(x)
    return post_list
