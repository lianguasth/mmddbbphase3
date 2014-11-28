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
#IFS='/' read -ra ADDR <<< "$1"
#IFS='.' read -ra ADDRR <<< "${ADDR[1]}"
#NAME="${ADDRR[0]}"
#echo $1
#cat $1/conncomp-kcore.csv | python lib/plotCommponent.py pic/plotKcore$NAME.png true
python ./lib/plotAll.py ./output/ conncomp-kcore.csv
#draw component
#cat $1/conncomp.csv | python lib/plotCommponent.py pic/plotConncomp$NAME.png true
python ./lib/plotAll.py ./output/ conncomp.csv
#draw degree
#cat $1/degreedist.csv | python lib/plotDegree.py pic/DegreeDist$NAME.png true
python ./lib/plotAll.py ./output/ degreedist.csv
#draw radius 
#cat $1/radius.csv | python lib/plotRadius.py pic/Radius$NAME.png true
#draw pagerank
#cat $1/pagerank.csv | python lib/plotPagerank.py pic/pageRank$NAME.png false
python ./lib/plotAll.py ./output/ pagerank.csv
}

main $1
