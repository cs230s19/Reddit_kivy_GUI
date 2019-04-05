import praw

reddit = praw.Reddit(client_id='5gcyUe_9oxJjBQ',
                         client_secret='wDZk9NXJrUTUJqu4yh3q1y8P01g',
                         password='VjGT4m5Uh7AQ',
                         user_agent='testapp',
                         username='progres5ion')


def get_redditor_info(redditusername):
    redditor_link_karmar = str(reddit.redditor(redditusername).link_karma)
    redditor_name = reddit.redditor(redditusername).name
    redditor_comment_karma = str(reddit.redditor(redditusername).comment_karma)

    redditor_profile = " "
    redditor_profile += "Redditor Name: " + redditor_name + "\n Redditor Comment Karma: " + redditor_comment_karma +\
                        "\n Link Karma: " + redditor_link_karmar

    return redditor_profile
