# language analysis of the comments of 4 subreddits: r/antiwork, r/productivity, r/psychic and r/skeptic
import os, os.path
import nltk
from nltk import word_tokenize
import nltk.data
from nltk.probability import ConditionalFreqDist
from nltk.probability import FreqDist
from nltk.tag import pos_tag
import praw
import pandas as pd


path = os.path.expanduser('~/nltk_data')

# access reddit 
reddit = praw.Reddit(client_id='8n0q-yj901hEsQ', 
                     client_secret='UIowXBsxjC-Q2Q9lZ1gVS7960HQ', \
                     user_agent='Productivity_NLP')


# assign initalising variables to the four subreddits - connect to them via reddit API
antiwork = reddit.subreddit('antiwork')
productivity = reddit.subreddit('productivity')
psychic = reddit.subreddit('psychic')
skeptic = reddit.subreddit('skeptic')


#[submission.comments for submission in antiwork.top(limit=10)]

antiwork = antiwork.comments(limit=300)
productivity = productivity.comments(limit=300)
psychic = psychic.comments(limit=300)
skeptic = skeptic.comments(limit=300)

# string to filter out in productivity data
discord_string = "Did you know /r/Productivity has an official Discord server?"

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

#print(tagged_antiwork)

noun_tags = ['NN', 'NNS', 'NNP', 'NNPS'] # noun singular, noun plural, proper noun singular, proper noun plural
verb_tags = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"] # verb base, verb PST tense, verb gerund/progressive, verb PST participle, verb sing. PRES
adj_tags = ["JJ", "JJR", "JJS"] # adj, adj comparative, adj superlative


# find nouns, verbs, adjectives for any community

def find_nouns(community):
  return nltk.FreqDist([x[0] for x in community if x[1] in noun_tags and len(x[0]) > 2 and x[0] != "https"])

def find_verbs(community):
  return nltk.FreqDist([x[0] for x in community if x[1] in verb_tags and len(x[0]) > 2 and x[0] != "https"])

def find_adjs(community):
  return nltk.FreqDist([x[0] for x in community if x[1] in adj_tags and len(x[0]) > 2 and x[0] != "https"])


# antiwork frequency distribution (nouns/verbs/adjectives)

antiwork_nouns = nltk.FreqDist(find_nouns(tagged_antiwork))
antiwork_verbs = nltk.FreqDist(find_verbs(tagged_antiwork))
antiwork_adjs = nltk.FreqDist(find_adjs(tagged_antiwork))

# productivity frequency distribution (nouns/verbs/adjectives)

productivity_nouns = nltk.FreqDist(find_nouns(tagged_productivity))
productivity_verbs = nltk.FreqDist(find_verbs(tagged_productivity))
productivity_adjs = nltk.FreqDist(find_adjs(tagged_productivity))

# psychic frequency distribution (nouns/verbs/adjectives)

psychic_nouns = nltk.FreqDist(find_nouns(tagged_psychic))
psychic_verbs = nltk.FreqDist(find_verbs(tagged_psychic))
psychic_adjs = nltk.FreqDist(find_adjs(tagged_psychic))

# skeptic frequency distribution (nouns/verbs/adjectives)

skeptic_nouns = nltk.FreqDist(find_nouns(tagged_skeptic))
skeptic_verbs = nltk.FreqDist(find_verbs(tagged_skeptic))
skeptic_adjs = nltk.FreqDist(find_adjs(tagged_skeptic))


# PLOTTING GRAPHS

#skeptic_adjs.plot(30, cumulative=False, title="Skeptic Adjectives")
#psychic_adjs.plot(30, cumulative=False, title="Psychic Adjectives")

#skeptic_nouns.plot(20, cumulative=False, title="Skeptic Nouns")
#psychic_nouns.plot(20, cumulative=False, title="Psychic Nouns")

productivity_nouns.plot(20, cumulative=False, title="Top 20 /r/productivity nouns")
antiwork_nouns.plot(20, cumulative=False, title="Top 20 /r/antiwork nouns")
psychic_nouns.plot(20, cumulative=False, title="Top 20 /r/psychic nouns")
skeptic_nouns.plot(20, cumulative=False, title="Top 20 /r/skeptic nouns")


