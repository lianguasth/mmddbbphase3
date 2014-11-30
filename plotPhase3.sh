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
plot $1
}

function main(){
	traverse $1
}


function plot(){
#draw kcore
python ./lib/plotAll.py $1 conncomp-kcore.csv
#draw component
python ./lib/plotAll.py $1 conncomp.csv
#draw degree
python ./lib/plotAll.py $1 degreedist.csv
#draw pagerank
python ./lib/plotAll.py $1 pagerank.csv
#draw indegree
python ./lib/plotAll.py $1 indegreedist.csv
#draw outdegree
python ./lib/plotAll.py $1 outdegreedist.csv
#draw triangle count
python ./lib/plotAll.py res triangle
#draw eigen vector
python ./lib/plotAll.py $1 eigvec.csv
}

main $1
