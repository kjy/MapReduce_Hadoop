#!/usr/bin/python

import sys

highestSale = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    thisSale = float(thisSale)
    if thisSale > highestSale:
        highestSale = thisSale

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", highestSale
        oldKey = thisKey
        highestSale = 0
       
    oldKey = thisKey


if oldKey != None:
    print oldKey, "\t", highestSale

"""
Answers:

Reno: 499.99
Toledo: 499.98
Chandler: 499.98

"""
