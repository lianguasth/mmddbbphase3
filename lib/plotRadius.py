#!/bin/python
import numpy as np
import render
import sys
import collections as co

def mergeFile():
	lists = {}
	x = []
	y = []
	for line in sys.stdin.readlines():
		line = line.strip()
		words = line.split(",")
		if len(words) == 2:
			ind = int(words[1])
			if(not lists.has_key(ind)):
				lists[ind] = 0
			lists[ind] = lists[ind] + 1
	#component number and size
	return lists


if __name__ == "__main__":
	x = []
	y = []
	fileName = sys.argv[1]
	lists = mergeFile()
	#sort the key
	od = co.OrderedDict(sorted(lists.items()))
	for key in od:
		print "%d, %d" % (key, lists[key])
		x.append(key)
		y.append(lists[key])
	render.render(x, y, 'Radius', 'Radius', 'Count', fileName)
