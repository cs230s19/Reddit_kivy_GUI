import praw

reddit = praw.Reddit(client_id='5gcyUe_9oxJjBQ',
                         client_secret='wDZk9NXJrUTUJqu4yh3q1y8P01g',
                         password='VjGT4m5Uh7AQ',
                         user_agent='testapp',
                         username='progres5ion')

redditusername = 'progres5ion'
print(reddit.redditor(redditusername).link_karma)
print(reddit.redditor(redditusername).name)
print('\n')

