set term png size 600,350 medium
set colors classic
set output 'lightcurve.png'
set xlabel 'JD-2447765.43500'
set ylabel 'mag'
set format y '%5.2f'
set xrange [-2357.17935:2836.06035]
set yrange [15.16:14.76]
plot "lightcurve.dat" using ($1)-2447765.43500:2 linecolor 2 pointtype 5 pointsize 0.3  title ""