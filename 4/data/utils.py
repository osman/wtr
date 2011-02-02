#!/usr/bin/env python

from re import findall
from constants import *
from sentiment_words import words

#Flip a sentiment score (as result of a negation)
def flip(s):
    return neg if s==pos else pos if s==neg else neutral

#Get the number of negations for a given word in a set of tokens
def num_negd(i, tokens):
    return len(set(tokens[(0 if i-3<0 else i-3):i]) & NEGATION_WORDS)

#Get a string representation of the sentiment
#if there or negation words, then flip the sentiment
def check_negd(word, num_neg):
    return str(flip(words[word]) if num_neg>0 else words[word])

#Get a string representation of the sentiment
#if there or negation words, then flip the sentiment only if there
#is an odd number of negations
def check_double_negd(word, num_neg):
    return str(flip(words[word]) if num_neg%2 else words[word])

#Make a guess
def naive_classify(text):
    sent_tokens = findall(TOPTERMS_REGEX, text)
    sentiment   = list(set(sent_tokens) & set(words.keys()))
    sentiment   = [check_negd(w,0) for w in sentiment]

    #Count the number of positive and negative sentiments
    sentiment   = ' '.join(sentiment)
    return {neg:sentiment.count(str(neg)), pos:sentiment.count(str(pos))}


def naive_negd_classify(text):
    sent_tokens = findall(TOPTERMS_REGEX, text)
    sentiment   = list(set(sent_tokens) & set(words.keys()))
    sentiment   = [(w, sent_tokens.index(w)) for w in sentiment]
    sentiment   = [check_negd(w, num_negd(i, sent_tokens)) for (w,i) in sentiment]

    #Count the number of positive and negative sentiments
    sentiment   = ' '.join(sentiment)
    return {neg:sentiment.count(str(neg)), pos:sentiment.count(str(pos))}

def naive_double_negd_classify(text):
    sent_tokens = findall(TOPTERMS_REGEX, text)
    sentiment   = list(set(sent_tokens) & set(words.keys()))
    sentiment   = [(w, sent_tokens.index(w)) for w in sentiment]
    sentiment   = [check_double_negd(w, num_negd(i, sent_tokens)) for (w,i) in sentiment]

    #Count the number of positive and negative sentiments
    sentiment   = ' '.join(sentiment)
    return {neg:sentiment.count(str(neg)), pos:sentiment.count(str(pos))}
