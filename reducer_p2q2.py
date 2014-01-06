#!/usr/bin/python

import sys

countTotal = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisCount = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", countTotal
        oldKey = thisKey
        countTotal = 0

    oldKey = thisKey
    countTotal += int(thisCount)

if oldKey != None:
    print oldKey, "\t", countTotal


"""
How many hits were made by the IP address 10.99.99.186?
Answer: 6

"""


