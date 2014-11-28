#!/bin/python
import sys

QR = 0
nTriangle = 0
value = []
for line in sys.stdin.readlines():
	if line.startswith("Number of Triangles"):
		words = line.split("=")
		nTriangle = float(words[1].strip())
	if line.startswith("QR Algorithm Error"):
		words = line.split("=")
		QR = float(words[1].strip())
	if line.startswith("("):
		words = line.split(",")
		t = words[1].strip()
		value.append(float(t[:-1]))
		
print QR
print value
print nTriangle
	
	
