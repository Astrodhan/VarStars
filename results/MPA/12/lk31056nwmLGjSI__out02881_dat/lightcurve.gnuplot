set term png size 600,350 medium
set colors classic
set output 'lightcurve.png'
set xlabel 'JD-2447062.49600'
set ylabel 'mag'
set format y '%5.2f'
set xrange [-1656.57610:3545.28210]
set yrange [17.74:16.19]
plot "lightcurve.dat" using ($1)-2447062.49600:2 linecolor 2 pointtype 5 pointsize 0.3  title ""