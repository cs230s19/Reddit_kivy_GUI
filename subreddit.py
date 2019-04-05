import praw

reddit = praw.Reddit(client_id='bFbCvelvrdVuFA',
                     client_secret='HjJOdVpi_jERV4T8PhAmxwtEM6w',
                     password='CaramelApple',
                     user_agent='testscript by /u/CS230_throwaway',
                     username='CS230_throwaway')


def get_posts(subreddit_name):
    num_stickied = 0
    num_posts = 10
    post_list = []

    hot_posts = reddit.subreddit(subreddit_name).hot(limit=num_posts)
    for x in hot_posts:
        if x.stickied:
            num_stickied += 1
    dict = reddit.subreddit(subreddit_name).hot(limit=num_posts + num_stickied)
    for x in dict:
        if not x.stickied:
            post_list.append(x)
    return post_list