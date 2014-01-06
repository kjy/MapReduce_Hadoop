"""
Write a MapReduce program which determines the number of hits to the site made by each
different IP address.

How many hits were made by the IP address 10.99.99.186?

"""


#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) > 1:
        ip = data[0]
        print "{0}\t{1}".format(ip, 1)


#Answer found in reducer_p2q2.py        

