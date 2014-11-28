import numpy
import matplotlib.pyplot as plt
import time

#plot the result
def render(x, y, title, xlabel, ylabel, fileName, setFlag = True):
	x = numpy.array(x)
	y = numpy.array(y)
	fig, ax = plt.subplots(1,1)
	ax.set_xscale("log")
	ax.set_yscale("log")
	#ax.set_xticks(numpy.arange(0,1,0.1))
	if setFlag:
		tma = max(y)
		plt.ylim(ymin=0.1, ymax=tma*10)
	plt.scatter(x,y)
	ax.grid()
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	#fig.show()
	fig.savefig(fileName, dpi=200)
#	raw_input()

if __name__ == "__main__":
	main(sys.argv)
