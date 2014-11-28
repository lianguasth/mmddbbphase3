import numpy as np
import renderScatter as render
import sys
import collections as co
lists = {}
x = []
y = []
#name of the png
fileName = sys.argv[1]
for line in sys.stdin.readlines():
	line = line.strip()
	words = line.split(",")
	if len(words) == 2:
		lists[float(words[0])] = float(words[1])
	#print lists[float(words(0))]
#sort the key
od = co.OrderedDict(sorted(lists.items()))
for key in od:
	x.append(key)
	y.append(lists[key])
#print x
#print y
render.render(x, y, 'Degree distribution', 'Degree', 'Count', fileName)
