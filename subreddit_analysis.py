# language analysis of the comments of 4 subreddits: r/antiwork, r/productivity, r/psychic and r/skeptic
import os, os.path
#from re import A
import nltk
from nltk import word_tokenize
import nltk.data
from nltk.probability import ConditionalFreqDist
from nltk.probability import FreqDist
from nltk.tag import pos_tag
import praw
import pandas as pd
from datetime import datetime


path = os.path.expanduser('~/nltk_data')

# access reddit 
reddit = praw.Reddit(client_id='8n0q-yj901hEsQ', 
                     client_secret='UIowXBsxjC-Q2Q9lZ1gVS7960HQ', \
                     user_agent='Productivity_NLP')


# get timestamps 
def get_yyyy_mm_dd_from_utc(dt):
    date = datetime.utcfromtimestamp(dt)
    
    return str(date.year) + "-" + str(date.month) + "-" + str(date.day)
 

# assign initalising variables to the four subreddits - connect to them via reddit API
antiwork = reddit.subreddit('antiwork')
productivity = reddit.subreddit('productivity')
psychic = reddit.subreddit('psychic')
skeptic = reddit.subreddit('skeptic')


#[submission.comments for submission in antiwork.top(limit=10)]

antiwork = antiwork.comments(limit=200)
productivity = productivity.comments(limit=200)
psychic = psychic.comments(limit=200)
skeptic = skeptic.comments(limit=200)

#for comment in productivity: #.comments.list():
  #print(comment.body)


    #all_comments = submission.comments.list()
    #print(all_comments)

    # https://praw.readthedocs.io/en/latest/tutorials/comments.html
#submission.comments.replace_more(limit=None)
#comment_body = ""

#for comment in submission.comments.list():
   # print(comment.body)
   # comment_body =  comment_body + comment.body + "\n"

#top_antiwork["z_comments"].append(comment_body)

#antiwork_data = pd.DataFrame(top_antiwork)

#for comment in antiwork.comments.list():
 # print(comment.body)
  #antiwork_comments = antiwork_comments + comment.body + "\n" 

# create corpora training data for each subreddit based on top-level comments
antiwork_corpus = [comment.body for comment in antiwork]
productivity_corpus = [comment.body for comment in productivity]
psychic_corpus = [comment.body for comment in psychic]
skeptic_corpus = [comment.body for comment in skeptic]

print(productivity_corpus)

# need to filter out:
#Did you know /r/Productivity has an official Discord server?\nJoin our Discord [here](https://discord.gg/productivity) and continue the conversation with over 5,000 members!\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/productivity) if you have any questions or concerns.*']
filter_comment = "Did you know /r/Productivity has an official Discord server?\nJoin our Discord [here](https://discord.gg/productivity) and continue the conversation with over 5,000 members!\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/productivity) if you have any questions or concerns.*"

def filter_discord_comment(filter_comment):
  filter_comment = ["Did you know /r/Productivity has an official Discord server?\nJoin our Discord [here](https://discord.gg/productivity) and continue the conversation with over 5,000 members!\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/productivity) if you have any questions or concerns.*"]
  if filter_comment in productivity_corpus:
    return True
  else:
    return False


productivity_data = list(filter(filter_discord_comment, productivity_corpus))
print(productivity_data)

# tokenize corpora
tokenized_antiwork = word_tokenize("".join(antiwork_corpus))
tokenized_productivity = word_tokenize("".join(productivity_corpus))
tokenized_psychic = word_tokenize("".join(psychic_corpus))
tokenized_skeptic = word_tokenize("".join(skeptic_corpus))

# tag corpus words for part of speech
tagged_antiwork = pos_tag(tokenized_antiwork)
tagged_productivity = pos_tag(tokenized_productivity)
tagged_psychic = pos_tag(tokenized_psychic)
tagged_skeptic = pos_tag(tokenized_skeptic)

# analyse frequency distribution of tokenized (untagged) words
#freq_antiwork = nltk.FreqDist(tokenized_antiwork)
#freq_productivity = nltk.FreqDist(tokenized_productivity)
#freq_psychic = nltk.FreqDist(tokenized_psychic)
#freq_skeptic = nltk.FreqDist(tokenized_skeptic)

#filter to only include words of more than length 3 chars
#antiwork_filter = dict([(m, n) for m, n in freq_antiwork.items() if len(m) > 3])
#productivity_filter = dict([(m, n) for m, n in freq_productivity.items() if len(m) > 3])
#psychic_filter = dict([(m, n) for m, n in freq_psychic.items() if len(m) > 3])
#skeptic_filter =  dict([(m, n) for m, n in freq_skeptic.items() if len(m) > 3])

 
#antiwork analysis.plot(50, cumulative=False, title="Antiwork Analysis")


#for key in sorted(antiwork_filter):
  # print("%s: %s" % (key, antiwork_filter[key]))


#for key in sorted(productivity_filter):
   #print("%s: %s" % (key, productivity_filter[key]))


#productivity_dist = nltk.FreqDist(productivity_filter)
#antiwork_dist = nltk.FreqDist(antiwork_filter)
#psychic_dist = nltk.FreqDist(psychic_filter)
#skeptic_dist = nltk.FreqDist(skeptic_filter)




#productivity_dist.plot(50, cumulative=False, title="Productivity Analysis")
#antiwork_dist.plot(50, cumulative=False, title="Antiwork Analysis")
#psychic_dist.plot(50, cumulative=False, title="Psychic Analysis")
#skeptic_dist.plot(50, cumulative=False, title="Skeptic Analysis")

# create dictionary storing topic info
"""
topics_dict = { "title":[], \
                "score":[], \
                "id":[], "url":[], \
                "comms_num": [], \
                "created": [], \
                "body":[]}"""

"""
for submission in top_antiwork:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

"""

