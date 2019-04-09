import praw

reddit = praw.Reddit(client_id='bFbCvelvrdVuFA',
                     client_secret='HjJOdVpi_jERV4T8PhAmxwtEM6w',
                     password='CaramelApple',
                     user_agent='testscript by /u/CS230_throwaway',
                     username='CS230_throwaway')


def get_redditor_info(redditusername):
    redditor_link_karmar = str(reddit.redditor(redditusername).link_karma)
    redditor_name = reddit.redditor(redditusername).name
    redditor_comment_karma = str(reddit.redditor(redditusername).comment_karma)

    redditor_profile = " "
    redditor_profile += "Redditor Name: " + redditor_name + "\n Redditor Comment Karma: " + redditor_comment_karma +\
                        "\n Link Karma: " + redditor_link_karmar
    return redditor_profile
