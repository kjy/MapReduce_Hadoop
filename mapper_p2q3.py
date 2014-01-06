"""

Find the most popular file on the Web site.  In other words, the file
which had the most hits.  Your Reducer should just write out the
name of the file and the number of hits into HDFS.

Full path to the most popular file:
Number of hits to that file:

"""

#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment



import sys
from urlparse import urlparse

for line in sys.stdin:
    line = line.strip()
    firstIndex = line.find("\"")
    lastIndex = line.rfind("\"")
    if (firstIndex > 1 and lastIndex > 2):
        requestString = line[firstIndex+1:lastIndex]
        actualUrl = requestString.split(" ")[1]
        docname = urlparse(actualUrl)
        print "{0}\t{1}".format(docname.path, 1)

#Answer found in reducer_p2q3.py
