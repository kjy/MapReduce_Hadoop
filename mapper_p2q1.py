"""

Write a MapReduce program which will display the number of hits for each
different file on the Web site.

How many hits were made to the page /assets/js/the-associates.js ?


"""
#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split("GET ")
    if len(data) > 1:
        file = data[1].split(" ")[0]
        print "{0}\t{1}".format(file, 1)
        

#Answer found in reducer_p2q1.py
        

