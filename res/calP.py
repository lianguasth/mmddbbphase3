#!/bin/bash
from os import listdir
from os.path import isfile, join
import sys

dic = {}
dirs = [ f for f in listdir(".") if  isfile(join(".",f)) ]
#print dirs
for thisFile in dirs:
#	print thisFile
	if not "triCount" in thisFile:
		pass
	else:
		tf = open(join(".", thisFile))
		line = tf.readline()
		tf.close()
		words = line.split("=")
		a = float(words[1])
		name = thisFile.split("_")[-1]
		dic[name] = a
#print dic

fnodeCount = open("./nodeCount.txt")
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

