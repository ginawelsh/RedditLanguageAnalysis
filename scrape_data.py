import praw
from praw.models import MoreComments

# connect to reddit

reddit = praw.Reddit(client_id=''
                     client_secret=''
                     user_agent='')

psychic = reddit.subreddit('psychic')
skeptic = reddit.subreddit('skeptic')


# scrape comment data from subreddit, store in text file (batch collection)

def scrape_comments(sub):
    for submission in sub.hot(limit=200):
        for comment in submission.comments:
            if isinstance(comment.body, MoreComments):
                continue
            with open(f"{sub}_data_store.txt", 'a') as fh:
                fh.write(comment.body + ' ')

#scrape_comments(psychic)
#scrape_comments(skeptic)
