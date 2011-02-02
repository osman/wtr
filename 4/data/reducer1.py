#!/usr/bin/env python

from sys import stdin

accurate = 0
recall = 0
time = 0.0
for line in stdin:
    (index, actual, s1, r1, s2, r2, s3, r3) = line.rstrip(' \\\\\n').split(' & ')

    if actual==s1: accurate += 1
    if (actual=='neutral') ^ (s1=='neutral'): recall += 1
    time += float(r1)

print '%d & %d & %.5f \\\\'%(accurate, 100-recall, time/100.0)
