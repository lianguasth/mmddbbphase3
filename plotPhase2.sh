#!/bin/bash
containsElement () {
  local e
  for e in "${@:2}"; do [[ "$e" == "$1" ]] && flag=0 && return; done
  flag=1
}
#draw kcore
IFS='/' read -ra ADDR <<< "$1"
IFS='.' read -ra ADDRR <<< "${ADDR[1]}"
NAME="${ADDRR[0]}"
DMAP=(output_cit-HepPh.txt output_cit-HepTh.txt output_p2p-Gnutella31.txt output_ca-AstroPh.txt output_email-EuAll.txt output_soc-Slashdot0811-75000.txt)
#echo $NAME
cat $1/conncomp-kcore.csv | python lib/plotCommponent.py pic/plotKcore$NAME.png true
#draw component
cat $1/conncomp.csv | python lib/plotCommponent.py pic/plotConncomp$NAME.png true
#draw degree
#echo "${ADDR[1]}"
#echo "${DMAP[@]}"
containsElement "${ADDR[1]}" "${DMAP[@]}"
echo "${flag}"
if [[ "${flag}" -eq 0 ]]
then
	#draw indegree
	cat $1/indegreedist.csv | python lib/plotIndegree.py pic/IndegreeDist$NAME.png true
	#draw outdegree
	cat $1/outdegreedist.csv | python lib/plotOutdegree.py pic/OutdegreeDist$NAME.png true
fi
cat $1/degreedist.csv | python lib/plotDegree.py pic/DegreeDist$NAME.png true
#draw
cat $1/radius.csv | python lib/plotRadius.py pic/Radius$NAME.png true
#draw pagerank
cat $1/pagerank.csv | python lib/plotPagerank.py pic/pageRank$NAME.png false
