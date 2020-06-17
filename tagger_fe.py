import pandas
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
import string
from nltk.corpus import stopwords

import sqlite3
import pandas as pd

#Setting Up

example = "Bike rentals near San Diego.1"

example_path = 'emails.db3'

cursor = sql_connect.cursor()

sql_connect = sqlite3.connect(example_path)

#Functions

def clean_search_string(term):
    # split into words
    tokens = word_tokenize(term)
    # convert to lower case
    tokens = [w.lower() for w in tokens]
    # remove punctuation from each word
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    # remove remaining tokens that are not alphabetic
    words = [word for word in stripped if word.isalpha()]
    # filter out stop words
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    return(words)

def returns_term_df(term):
    '''takes a term and returns a dataframe of emails where that term is included'''
    query = "SELECT * FROM factbook;"

def return_searched_emails(terms, path)
    '''takes a list of search terms and a path, returns emails'''
    for term in terms:



