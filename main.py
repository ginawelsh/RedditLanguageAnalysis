# language analysis of the comments of 4 subreddits: r/antiwork, r/productivity, r/psychic and r/skeptic
import nltk
from nltk import word_tokenize
import nltk.data
from nltk.probability import FreqDist
from nltk.tag import pos_tag
import praw
import pandas as pd

# access reddit 
reddit = praw.Reddit(client_id='8n0q-yj901hEsQ', 
                     client_secret='UIowXBsxjC-Q2Q9lZ1gVS7960HQ', \
                     user_agent='Productivity_NLP')

# assign initalising variables to the four subreddits - connect to them via reddit API
antiwork = reddit.subreddit('antiwork')
productivity = reddit.subreddit('productivity')
psychic = reddit.subreddit('psychic')
skeptic = reddit.subreddit('skeptic')

# sample 300 comments from each subreddit

antiwork = antiwork.comments(limit=300)
productivity = productivity.comments(limit=300)
psychic = psychic.comments(limit=300)
skeptic = skeptic.comments(limit=300)

# string to filter out in productivity data
discord_string = "Did you know /r/Productivity has an official Discord server?"


# return raw text from comments

def return_comments(community):
  return [comment.body for comment in community if discord_string not in comment.body]

# create corpora training data for each subreddit based on top-level comments - left untokenized here in case of syntactic analysis
antiwork_corpus = return_comments(antiwork)
productivity_corpus = return_comments(productivity)
psychic_corpus = return_comments(psychic)
skeptic_corpus = return_comments(skeptic)

# tokenize corpora

def tokenize(community):
  return word_tokenize("".join(community))

tokenized_antiwork = tokenize(antiwork_corpus)
tokenized_productivity = tokenize(productivity_corpus)
tokenized_psychic = tokenize(psychic_corpus)
tokenized_skeptic = tokenize(skeptic_corpus)

# tag corpus words for part of speech
tagged_antiwork = pos_tag(tokenized_antiwork)
tagged_productivity = pos_tag(tokenized_productivity)
tagged_psychic = pos_tag(tokenized_psychic)
tagged_skeptic = pos_tag(tokenized_skeptic)


tagged_examples = open("tagged_examples.txt", "w")

for i in tagged_productivity:
  tagged_examples.write(str(i) + '\n')



# PARTS OF SPEECH

# noun singular, noun plural, proper noun singular, proper noun plural
nouns = ['NN', 'NNS', 'NNP', 'NNPS'] 

# verb base, verb PST tense, verb gerund/progressive, verb PST participle, verb sing. PRES
verbs = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"] 

# adj, adj comparative, adj superlative
adjs = ["JJ", "JJR", "JJS"] 


# find nouns, verbs, adjectives for any community

def find_tags(community, pos_tag):
  return nltk.FreqDist([x[0] for x in community if x[1] in pos_tag and len(x[0]) > 2 and x[0] != "https"])

# antiwork frequency distribution (nouns/verbs/adjectives)

antiwork_nouns = nltk.FreqDist(find_tags(tagged_antiwork, nouns))
antiwork_verbs = nltk.FreqDist(find_tags(tagged_antiwork, verbs))
antiwork_adjs = nltk.FreqDist(find_tags(tagged_antiwork, adjs))

# productivity frequency distribution (nouns/verbs/adjectives)

productivity_nouns = nltk.FreqDist(find_tags(tagged_productivity, nouns))
productivity_verbs = nltk.FreqDist(find_tags(tagged_productivity, verbs))
productivity_adjs = nltk.FreqDist(find_tags(tagged_productivity, adjs))

# psychic frequency distribution (nouns/verbs/adjectives)

psychic_nouns = nltk.FreqDist(find_tags(tagged_psychic, nouns))
psychic_verbs = nltk.FreqDist(find_tags(tagged_psychic, verbs))
psychic_adjs = nltk.FreqDist(find_tags(tagged_psychic, adjs))

# skeptic frequency distribution (nouns/verbs/adjectives)

skeptic_nouns = nltk.FreqDist(find_tags(tagged_skeptic, nouns))
skeptic_verbs = nltk.FreqDist(find_tags(tagged_skeptic, verbs))
skeptic_adjs = nltk.FreqDist(find_tags(tagged_skeptic, adjs))

# PLOTTING TOP 20 GRAPHS

# TOP 20 NOUNS 
productivity_nouns.plot(20, cumulative=False, title="Top 20 /r/productivity nouns")
antiwork_nouns.plot(20, cumulative=False, title="Top 20 /r/skeptic nouns")

# TOP 20 VERBS

productivity_verbs.plot(20, cumulative=False, title="Top 20 /r/productivity verbs")
antiwork_verbs.plot(20, cumulative=False, title="Top 20 /r/antiwork verbs")

# TOP 20 ADJECTIVES

productivity_adjs.plot(20, cumulative=False, title="Top 20 /r/productivity adjectives")
antiwork_adjs.plot(20, cumulative=False, title="Top 20 /r/antiwork adjectives")