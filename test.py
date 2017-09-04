import nltk
import string
import os
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.cluster import KMeans
from pylab import *

path = '/home/nishantkr/Desktop/doc'
token_dict = {}
stemmer = PorterStemmer()

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems

for subdir, dirs, files in os.walk(path):
    for file in files:
        file_path = subdir + os.path.sep + file
        shakes = open(file_path, 'r')
        text = shakes.read()
        lowers = text.lower()
        no_punctuation = lowers.translate(None, string.punctuation)
        token_dict[file] = no_punctuation
        
#vectoriser
tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs = tfidf.fit_transform(token_dict.values())
#print token_dict.values() #This method returns a list of all the values available in dictionary.
print(tfs.shape)

num_clusters=input("Enter number of clusters you want\n");
km=KMeans(n_clusters=num_clusters)
km.fit(tfs)
clusters=km.labels_.tolist()

print("Top terms per cluster:")
#sort cluster centers by proximity to centroid
order_centroids = km.cluster_centers_.argsort()[:, ::-1]
terms = tfidf.get_feature_names()
for i in range(num_clusters):
    print "Cluster %d:" % i,
    for ind in order_centroids[i, :10]:#replace 6 with n words per cluster
        print ' %s' % terms[ind],
    print
#-----------------------------------------------------------------------
