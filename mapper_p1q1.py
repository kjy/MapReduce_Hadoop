"""
Now it's time for you to have a go at this. For starters you will have to work with the same data set - sales data,
that we discussed in lessons. You will have to write some Mappers and Reducers yourself and then answer the questions
about data that follow. You will have to do the data processing on your local pseudo-distributed cluster,
but you will be able to see if your solution was correct by submitting your results to our system.

The three questions that you have to answer about this data set are:

Instead of breaking the sales down by store, instead give us a sales breakdown by product category across all of our stores.
Find the monetary value for the highest individual sale for each separate store.
Find the total sales value across all the stores, and the total number of sales. Assume there is only one reducer.
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
        print "{0}\t{1}".format(item,cost)


#Answer to question to found in reducer_p1q1.py
