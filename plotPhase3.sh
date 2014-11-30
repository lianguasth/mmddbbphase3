#!/bin/bash

function traverse() {
	
for file in `ls $1`
do
	#echo "${1}/${file}"
	if [ ! -d "${1}/${file}" ] ; then
		echo "${1}/${file}"
		IFS='.' read -ra ADDR <<< "${file}"
		NAME="${ADDR[0]}"
		cat "${1}/${file}" | grep 'Number of Triangles' > res/triCount_$NAME
	fi
done
plot
}

function main(){
	traverse $1
}


function plot(){
#draw kcore
python ./lib/plotAll.py ./output/ conncomp-kcore.csv
#draw component
python ./lib/plotAll.py ./output/ conncomp.csv
#draw degree
python ./lib/plotAll.py ./output/ degreedist.csv
#draw pagerank
python ./lib/plotAll.py ./output/ pagerank.csv
#draw indegree
python ./lib/plotAll.py ./output/ indegreedist.csv
#draw outdegree
python ./lib/plotAll.py ./output/ outdegreedist.csv
#draw triangle count
python ./lib/plotAll.py res triangle
#draw eigen vector
#python ./lib/plotAll.py ./output/ eigvec.csv
}

main $1
