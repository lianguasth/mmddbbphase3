#!/bin/bash
#draw kcore
IFS='/' read -ra ADDR <<< "$1"
IFS='.' read -ra ADDRR <<< "${ADDR[1]}"
NAME="${ADDRR[0]}"
#echo $NAME
cat $1/conncomp-kcore.csv | python lib/plotCommponent.py pic/plotKcore$NAME.png true
#draw component
cat $1/conncomp.csv | python lib/plotCommponent.py pic/plotConncomp$NAME.png true
#draw degree
cat $1/degreedist.csv | python lib/plotDegree.py pic/DegreeDist$NAME.png true
#draw 
cat $1/radius.csv | python lib/plotRadius.py pic/Radius$NAME.png true
#draw pagerank
cat $1/pagerank.csv | python lib/plotPagerank.py pic/pageRank$NAME.png false
