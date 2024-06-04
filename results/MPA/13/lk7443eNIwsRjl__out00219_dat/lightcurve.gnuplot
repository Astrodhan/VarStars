set term png size 600,350 medium
set colors classic
set output 'lightcurve.png'
set xlabel 'JD-2447035.45800'
set ylabel 'mag'
set format y '%5.2f'
set xrange [-1629.53810:3572.32010]
set yrange [15.65:14.80]
plot "lightcurve.dat" using ($1)-2447035.45800:2 linecolor 2 pointtype 5 pointsize 0.3  title ""