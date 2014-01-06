

"""
Find the monetary value for the highest individual sale for each
separate store.What are the values for the following stores?

Reno
Toledo
Chandler

"""


#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(store, cost)


#Answers to the above question are found in reducer_p1q2.py
