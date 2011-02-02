#!/usr/bin/env python

from sys import stdin

count = 0
for line in stdin:
    if line.find('^')!=-1: continue

    for word in [' is ', ' isnt ', ' tmr ', ' like ', ' hey ', ' yeah ', ' yea ']:
        s = line.rstrip('\n').replace('$','\\$').replace('#','\\#').replace('%','\\%').replace('&','\\&').replace('_','\\_').replace('^','\\^')
        if word in line:
            count += 1
            print '''%d & %s & \\\\'''%(count, s)
            break
    if count==100: break
