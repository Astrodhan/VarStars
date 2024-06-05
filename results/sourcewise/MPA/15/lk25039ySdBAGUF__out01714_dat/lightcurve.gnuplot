set term png size 600,350 medium
set colors classic
set output 'lightcurve.png'
set xlabel 'JD-2445947.49300'
set ylabel 'mag'
set format y '%5.2f'
set xrange [-541.57310:4660.28510]
set yrange [15.73:15.17]
plot "lightcurve.dat" using ($1)-2445947.49300:2 linecolor 2 pointtype 5 pointsize 0.3  title ""