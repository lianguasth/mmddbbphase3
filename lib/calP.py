#!/bin/bash
from os import listdir
from os.path import isfile, join
import sys

dic = {}
dirs = [ f for f in listdir(sys.argv[1]) if  isfile(join(sys.argv[1],f)) ]
#print dirs
for thisFile in dirs:
#	print thisFile
	if not "triCount" in thisFile:
		pass
	else:
		tf = open(join(sys.argv[1], thisFile))
		line = tf.readline()
		tf.close()
		#print line
		#print thisFile
		words = line.split("=")
		a = float(words[1])
		name = thisFile.split("_")[-1]
		dic[name] = a
#print dic

fnodeCount = open(join(sys.argv[1],"nodeCount.txt"))
lines = fnodeCount.readlines();
fnodeCount.close()

for line in lines:
	line = line.strip()
	words = line.split(":")
	fName = words[0].strip()
	nNode = int(words[1].strip())
	ff = fName.split("_");
	#print ff
	fff = "".join(ff[1:])
	#print fff[:-4]
	s = fff[:-4].split(".")[0]
	#print s
	print "%s\t%f"%(s, dic[s]/float(nNode))
