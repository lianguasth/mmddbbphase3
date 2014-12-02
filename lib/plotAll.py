from os import listdir
from os.path import isfile, join
import sys
import collections as co
import numpy
import matplotlib.pyplot as plt
import pandas as pd

dMap = ['cit-HepPh.txt', 'cit-HepTh.txt', 'p2p-Gnutella31.txt', 'ca-AstroPh.txt',\
 'email-EuAll.txt', 'soc-Slashdot0811-75000.txt', 'cit-Cora.txt', 'soc-digg.txt', \
 'soc-flickr-75000.txt', 'soc-pokec-75000.txt','soft-jdkdependency.txt',\
 'text-spanishbook.txt']

def isDirected(name):
	#print name
 	for ss in dMap:
 		if ss in name:
 			return True
 	return False

def calDegreeStat(degree, count):
	#find max degree
	mdegree = max(degree)
	#find degree with most count
	indMCount = count.index(max(count))
	#calculate average degree
	avgDegree = float(sum(degree))/float(len(degree))
	#calculate the zero degree
	res = "maxDegr %d\nmostDegr %d\navgDegr %.2f"\
	%(mdegree, degree[indMCount], avgDegree)
	if 0 in degree:
		res = "%s \nnZeroDegr %d"%(res, count[degree.index(0)])
	#print res
	return res

def calStatComp(comp, count):
	if not comp:
		return None
	size = sum(count)
	mcomp = max(comp)
	res = "compCount %d\nmaxComp %d\n"\
	%(size, mcomp)
	return res


def plotDegree(dirs, path1, path2, plt, fig, ax):
	ox = 1
	oy = 1
	fnTotalNode = join("res", "nodeCount.txt")
	fNode = open(fnTotalNode, 'w+')
	for thisDir in dirs:
		lists = {}
		x = []
		y = []
		print join(path1, thisDir, path2)
		ff = open(join(path1, thisDir, path2))
		#name of the png
		nNode = 0
		fileName = path2
		for line in ff.readlines():
			line = line.strip()
			words = line.split(",")
			if len(words) == 2:
				lists[float(words[0])] = float(words[1])
				nNode = nNode + int(words[1])
			#print lists[float(words(0))]
		fNode.write("%s : %d\n"%(thisDir, nNode))
		#sort the key
		od = co.OrderedDict(sorted(lists.items()))
		for key in od:
			x.append(key)
			y.append(lists[key])
		msg = calDegreeStat(x,y)
		#print x
		#print y
		renderScatter(x, y, 'Degree distribution', 'Degree', 'Count', \
			thisDir[7:-4], ox-1, oy-1, plt, fig, ax, message = msg)
		if ox == 5:
			ox = 1
			oy = oy + 1
		else:
			ox = ox + 1
		ff.close()
	fNode.close()


def plotIndeg(dirs, path1, path2, plt, fig, ax):
	ox = 1
	oy = 1
	for thisDir in dirs:
		if not isDirected(thisDir):
			continue
		lists = {}
		x = []
		y = []
		#print join(path1, thisDir, path2)
		ff = open(join(path1, thisDir, path2))
		#name of the png
		fileName = path2
		for line in ff.readlines():
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
		#print thisDir
		msg = calDegreeStat(x, y)
		renderScatter(x, y, 'InDegree distribution', 'indegree', 'Count', \
			thisDir[7:-4], ox-1, oy-1, plt, fig, ax, message=msg)
		if ox == 3:
			ox = 1
			oy = oy + 1
		else:
			ox = ox + 1
		ff.close()


def plotOutdeg(dirs, path1, path2, plt, fig, ax):
	ox = 1
	oy = 1
	for thisDir in dirs:
		if not isDirected(thisDir):
			continue
		lists = {}
		x = []
		y = []
		#print join(path1, thisDir, path2)
		ff = open(join(path1, thisDir, path2))
		#name of the png
		fileName = path2
		for line in ff.readlines():
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
		msg = calDegreeStat(x, y)
		renderScatter(x, y, 'Outdegree distribution', 'OutDegree', \
			'Count', thisDir[7:-4], ox-1, oy-1, plt, fig, ax, message=msg)
		if ox == 3:
			ox = 1
			oy = oy + 1
		else:
			ox = ox + 1
		ff.close()


def plotComp(dirs, path1, path2, plt, fig, ax):
	ox = 1
	oy = 1
	for thisDir in dirs:
		lists = {}
		x = []
		y = []
		print join(path1, thisDir, path2)
		ff = open(join(path1, thisDir, path2))
		#name of the png
		fileName = path2
		lists = mergeFile(ff)
		alists = mergeList(lists)
		od = co.OrderedDict(sorted(alists.items()))
		for key in od:
			x.append(key)
			y.append(alists[key])
		msg = calStatComp(x, y)
		if msg is not None:
			renderScatter(x, y, 'kcore', 'kcore', 'Count', thisDir[7:-4], ox-1,\
		 oy-1, plt, fig, ax, False, message=msg, annoX = max(x), annoY = max(y))
		else:
			renderScatter(x, y, 'kcore', 'kcore', 'Count', thisDir[7:-4], ox-1,\
		 oy-1, plt, fig, ax, False)
		if ox == 5:
			ox = 1
			oy = oy + 1
		else:
			ox = ox + 1
		ff.close()

def plotPagerank(dirs, path1, path2, plt, fig, ax):
	ox = 1
	oy = 1
	for thisDir in dirs:
		x = []
		y = []
		print join(path1, thisDir, path2)
		ff = open(join(path1, thisDir, path2))
		#name of the png
		fileName = path2
		for line in ff.readlines():
			line = line.strip()
			words = line.split(",")
			if len(words) == 2:
				y.append(float(words[1]))
		x = [i+1 for i in range(len(y))]
		y = sorted(y, reverse=True)
		#print len(y)
		#print x
		#print y
		render(x, y, 'pagerank', 'pagerank', 'Score', thisDir[7:-4], ox-1,\
		 oy-1, plt, fig, ax, False)
		if ox == 5:
			ox = 1
			oy = oy + 1
		else:
			ox = ox + 1
		ff.close()


def calCorr(x , y):
	total = 0
	xx = []
	yy = []
	for tid in range(len(x)):
		xx.append(numpy.abs(x[tid]))
		yy.append(numpy.abs(y[tid]))
	return numpy.abs(numpy.corrcoef(xx, yy)[0][1])


#draw out eigen value
def plotEigen(dirs, path1, path2, plt, fig, ax):
	ox = 1
	oy = 1
	for thisDir in dirs:
		vectors = []
		x = {}
		vt = -1;
		print join(path1, thisDir, path2)
		ff = open(join(path1, thisDir, path2))
		#name of the png
		fileName = path2
		for line in ff.readlines():
			line = line.strip()
			words = line.split(",")
			if len(words) == 3:
				tid = words[0];
				tcol = int(words[1])
				tval = float(words[2])
				if tcol is not vt:
					vt = tcol
					if x:
						vectors.append(x.copy())
					x = {}
				x[tid] = tval
		vectors.append(x.copy())
		minTotal = 100000000
		#print len(vectors)
		for i in range(len(vectors)):
			xi = vectors[i]
			#print xi
			#raw_input()
			for j in range(i+1, len(vectors)):
				xj = vectors[j]
				#print xj
				#raw_input()
				total = calCorr(xi, xj)
				#print numpy.corrcoef(xi,xj)
				#total = numpy.corrcoef(xi,xj)[0][1]
				#print total
				if total < minTotal:
					minTotal = total
					mx = xi
					my = xj
		#for the test
		#mx = vectors[1]
		#my = vectors[2]
		xx = []
		yy = []
		for tid in mx.keys():
			#if mx[tid] < 0.2 and my[tid] < 0.2:
			xx.append(mx[tid])
			yy.append(my[tid])
		renderScatter(xx, yy, 'eigenVector', 'eigenVector', 'pair', \
			thisDir[7:-4], ox-1, oy-1, plt, fig, ax, False, False)
		if ox == 5:
			ox = 1
			oy = oy + 1
		else:
			ox = ox + 1
		ff.close()


#draw out eigen value using 4 vector
def plotEigenRev(dirs, path1, path2, plt, fig, ax):
	ox = 1
	oy = 1
	for thisDir in dirs:
		vectors = []
		vt = -1;
		print join(path1, thisDir, path2)
		ff = open(join(path1, thisDir, path2))
		#name of the png
		fileName = path2
		for line in ff.readlines():
			line = line.strip()
			words = line.split(",")
			if len(words) == 3:
				tid = words[0];
				tcol = int(words[1])
				tval = float(words[2])
				vectors.append(tval)
		#num = int(len(vectors)/4)
		num = int(len(vectors)/3)
		vectorR = []
		for i in range(3):
			t = []
			for j in range(num):
				t.append(vectors[i*num + j])
			vectorR.append(t)
		minTotal = 100000000
		#print len(vectors)
		#for i in range(0,3):
		for i in range(0,2):
			xi = vectorR[i]
			#print xi
			#raw_input()
			#for j in range(i+1, 4):
			for j in range(i+1, 3):
				xj = vectorR[j]
				#print xj
				#raw_input()
				total = calCorr(xi, xj)
				#print numpy.corrcoef(xi,xj)
				#total = numpy.corrcoef(xi,xj)[0][1]
				#print total
				if total < minTotal:
					minTotal = total
					mx = xi
					my = xj
		#for the test
		#mx = vectors[1]
		#my = vectors[2]
		renderScatter(mx, my, 'eigenVector', 'eigenVector', 'pair', \
			thisDir[7:-4], ox-1, oy-1, plt, fig, ax, False, False)
		if ox == 5:
			ox = 1
			oy = oy + 1
		else:
			ox = ox + 1
		ff.close()


#return a lists of component number \t size
def mergeFile(fil):
	lists = {}
	x = []
	y = []
	for line in fil.readlines():
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


#plot the result
def render(x, y, title, xlabel, ylabel, fileName, subX, subY, plt, fig, ax, setFlag = True):
	x = numpy.array(x)
	y = numpy.array(y)
	#print subX
	#print subY
	ax[subX, subY].set_xscale("log")
	ax[subX, subY].set_yscale("log")
	#ax[subX, subY].yaxis.tick_right()
	#ax.set_xticks(numpy.arange(0,1,0.1))
	if setFlag:
		tma = max(y)
		plt.ylim(ymin=0.1, ymax=tma*10)
	#ax[subX,subY].scatter(x,y, s = 1)
	ax[subX, subY].plot(x,y,'ro', ms = 1)
	ax[subX, subY].plot(x,y,'b-', ms = 1)
	ax[subX, subY].grid()
	ax[subX, subY].set_title(fileName, fontsize=10)
	#ax[subX, subY].xlabel(xlabel)
	ax[subX, subY].yaxis.set_label_position("right")
	ax[subX, subY].set_ylabel(ylabel, fontsize=10)


#plot the result
def renderScatter(x, y, title, xlabel, ylabel, fileName, subX,\
 subY, plt, fig, ax, setFlag = True, logScale = True, message = None, \
 annoX=10, annoY=10):
	x = numpy.array(x)
	y = numpy.array(y)

	#print subX
	#print subY
	if logScale:
		ax[subX, subY].set_xscale("log")
		ax[subX, subY].set_yscale("log")
	else:
		ax[subX, subY].tick_params(axis='x', labelsize=4)
		ax[subX, subY].tick_params(axis='y', labelsize=8)
	#ax[subX, subY].yaxis.tick_right()
	#ax.set_xticks(numpy.arange(0,1,0.1))
	if setFlag:
		tma = max(y)
		plt.ylim(ymin=0.1, ymax=tma*10)
	ax[subX,subY].scatter(x,y, s = 1)
	#ax[subX, subY].plot(x,y,'ro')
	#ax[subX, subY].plot(x,y,'b-')
	ax[subX, subY].grid()
	ax[subX, subY].set_title(fileName, fontsize=10)
	#ax[subX, subY].xlabel(xlabel)
	ax[subX, subY].yaxis.set_label_position("right")
	ax[subX, subY].set_ylabel(ylabel, fontsize=10)
	if message is not None:
		# ax[subX, subY].annotate(message, xy = (float(sum(x))/float(len(x))/3.0*5.0,max(y)), \
		# 	fontsize = 3,horizontalalignment='right', verticalalignment='top')
		ax[subX, subY].annotate(message, xy = (annoX,annoY), \
		 	fontsize = 3,horizontalalignment='right', verticalalignment='top')
#	fig.show()
#	fig.savefig(fileName, dpi=200)

def plotTri(targetDir, plt, fig, axx):
	x = []
	qq = []
	fs = [ f for f in listdir(targetDir) if isfile(join(sys.argv[1],f)) ]
	for f in fs:
		ff = open(join(targetDir,f))
		for line in ff.readlines():
			if "Triangle" in line:
				qq.append(f[16:])
				words = line.split("=")
				x.append(float(words[1].strip()))
		ff.close()
	#print x
	#ax.hist(x)
	#t = [i for i in range(len(x))]
	#ax.plot(t, x)
	data = pd.Series(x,index=qq)
	data.plot(kind='barh', ax=axx, fontsize=4)
	ax.set_title("Triangle Count Histogram")
	ax.set_xlabel("Triangle")
	ax.set_ylabel("Count")
	#plt.show()
	#raw_input()


fig, ax = plt.subplots(5, 4)
fig.tight_layout()
dirs = [ f for f in listdir(sys.argv[1]) if not isfile(join(sys.argv[1],f)) ]
if "indegree" in sys.argv[2]:
	fig, ax = plt.subplots(3, 4)
	fig.tight_layout()
	plotIndeg(dirs, sys.argv[1], sys.argv[2], plt, fig, ax)
elif "outdegree" in sys.argv[2]:
	fig, ax = plt.subplots(3, 4)
	fig.tight_layout()
	plotOutdeg(dirs, sys.argv[1], sys.argv[2], plt, fig, ax)
elif "degree" in sys.argv[2]:
	plotDegree(dirs, sys.argv[1], sys.argv[2], plt, fig, ax)
elif "kcore" in sys.argv[2]:
	plotComp(dirs, sys.argv[1], sys.argv[2], plt, fig, ax)
elif "pagerank" in  sys.argv[2]:
	plotPagerank(dirs, sys.argv[1], sys.argv[2], plt, fig, ax)
elif "conncomp" in sys.argv[2]:
	plotComp(dirs, sys.argv[1], sys.argv[2], plt, fig, ax)
elif "triangle" in sys.argv[2]:
	fig,ax = plt.subplots(1, 1)
	plotTri(sys.argv[1], plt, fig, ax)
elif "eigvec" in sys.argv[2]:
	plotEigenRev(dirs, sys.argv[1], sys.argv[2], plt, fig, ax)


#plt.show()
print join("pic", "%s.png"%(sys.argv[2][:-4]))
fig.savefig(join("pic", "%s.png"%(sys.argv[2][:-4])), dpi=200)
