import praw
# authentication token for reddit throwaway account
reddit = praw.Reddit(client_id='bFbCvelvrdVuFA',
                     client_secret='HjJOdVpi_jERV4T8PhAmxwtEM6w',
                     password='CaramelApple',
                     user_agent='testscript by /u/CS230_throwaway',
                     username='CS230_throwaway')


def get_redditor_info(redditusername):
    """
    get_redditor_info() function pulls user public attributes from reddit redditor object
    :param redditusername
    :return: redditor_profile - user account profile string object with link and comment karma
    """
    redditor_link_karmar = str(reddit.redditor(redditusername).link_karma)
    redditor_name = reddit.redditor(redditusername).name
    redditor_comment_karma = str(reddit.redditor(redditusername).comment_karma)

    redditor_profile = " "
    redditor_profile += "Redditor Name: " + redditor_name + "\n Redditor Comment Karma: " + redditor_comment_karma +\
                        "\n Link Karma: " + redditor_link_karmar
    return redditor_profile
