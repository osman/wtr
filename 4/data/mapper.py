#!/usr/bin/env python

from sys import stdin
from time import time

from constants import pos,neg
from utils import naive_classify as classify1
from utils import naive_negd_classify as classify2
from utils import naive_double_negd_classify as classify3

for line in stdin:
    (index, message, actual) = line.rstrip(' \\\\\n').split(' & ')

    #Run the same classification ten times to obtain an average runtime
    times = [[],[],[]]
    classification = [0,0,0]
    pos_count = [0,0,0]
    neg_count = [0,0,0]
    avg_runtime = [0,0,0]
    for i in xrange(1000):
        start = time()
        classification[0] = classify1(message.lower())
        end = time()
        times[0].append(end-start)
        
        start = time()
        classification[1] = classify2(message.lower())
        end = time()
        times[1].append(end-start)
        
        start = time()
        classification[2] = classify3(message.lower())
        end = time()
        times[2].append(end-start)

    #Classify the message with a sentiment
    for i in xrange(3):
        pos_count[i] = classification[i][pos]
        neg_count[i] = classification[i][neg]
        avg_runtime[i] = '%.5f'%sum(times[i])

    #Return a sentiment result for the message text
    result = [index, actual]
    for i in xrange(1,4):
        if   pos_count[-i]<neg_count[-i]:   result.insert(2,'negative')
        elif pos_count[-i]>neg_count[-i]:   result.insert(2,'positive')
        else:                       result.insert(2,'neutral')
        result.insert(3,avg_runtime[-i])
    print ' & '.join(result)+' \\\\'
