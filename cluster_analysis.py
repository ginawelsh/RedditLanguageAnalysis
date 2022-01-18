import nltk
from nltk import word_tokenize
import nltk.data
from nltk.probability import FreqDist
from nltk.tag import pos_tag
import praw
import pandas as pd
from four_subreddits import return_comments, tokenize, freq_words
