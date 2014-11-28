#!/bin/python
import numpy as np
import renderScatter as render
import sys
import collections as co

#return a lists of component number \t size
def mergeFile():
	lists = {}
	x = []
	y = []
	for line in sys.stdin.readlines():
		line = line.strip()
		words = line.split(",")
		if len(words) == 2:
			ind = words[1]
			#print ind
			if(not lists.has_key(ind)):
				lists[ind] = 0
			lists[ind] = lists[ind] + 1
	#component number and size
	return lists



def mergeList(oriList):
	lists = {}
	for key in oriList:
		ind = oriList[key]
		if(not lists.has_key(ind)):
			lists[ind] = 0
		lists[ind] = lists[ind] + 1
	return lists

if __name__ == "__main__":
	x = []
	y = []
	fileName = sys.argv[1]
	oriList = mergeFile()
	lists = mergeList(oriList)
	#sort the key
	#print len(lists)
	od = co.OrderedDict(sorted(lists.items()))
	for key in od:
		print "%d, %d" % (key, lists[key])
		x.append(key)
		y.append(lists[key])
	render.render(x, y, 'Weakly Connected Components', 'Component size', 'Count', fileName)
