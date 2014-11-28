import numpy as np
import render
import sys
import collections as co
x = []
y = []
#name of the png
fileName = sys.argv[1]
shouldScale = True
if sys.argv[2] == "false":
	shouldScale = False
for line in sys.stdin.readlines():
	line = line.strip()
	words = line.split(",")
	if len(words) == 2:
		y.append(float(words[1]))
	#print lists[float(words(0))]
#sort the key
x = [i+1 for i in range(len(y))]
y = sorted(y, reverse=True)
#print y
#print len(x)
#print len(y)
render.render(x, y, 'PageRank', 'Rank', 'PageRank value', fileName, shouldScale)
