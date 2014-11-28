##############################################
# by Danai Koutra, April 2013
# packaged by Christos Faloutsos, Oct. 2013
##############################################

set key top right box
set logscale xy 10
set format x "10^{%L}"
set format y "10^{%L}"
set log cb 10
set format cb "10^{%L}"

set terminal postscript enhanced eps 30 color

# to create matlab-like palette
set palette defined ( 0 '#000090',\
		      1 '#000fff',\
		      2 '#0090ff',\
		      3 '#0fffee',\
		      4 '#90ff70',\
		      5 '#ffee00',\
		      6 '#ff7000',\
		      7 '#ee0000',\
		      8 '#7f0000')

set view map
set pm3d map
set nokey


#########################################################
### start: edit this area

# set xlabel "x-axis"
# set ylabel "y-axis" -1.2,0
set title "y-stuff vs x-stuff"

### end: edit this area
#########################################################


#set xrange [x_min:x_max]
#set yrange [y_min:y_max]


set datafile separator ","
set output 'out_heatmap.eps'
splot filename using ($1+1):($2+1):3 with points notitle palette pt 7 ps 1


