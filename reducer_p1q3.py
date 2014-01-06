#!/usr/bin/python

import sys

salesTotal = 0
transactions = 0

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

    salesTotal += float(data_mapped[1])
    transactions += 1

print transactions, "\t", salesTotal


"""
Answer:

Number of Sales: 4138476

Total Value of Sales: 1034457953.26

"""
