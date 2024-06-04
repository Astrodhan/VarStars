set term png size 600,350 medium
set colors classic
set output 'lightcurve.png'
set xlabel 'JD-2447477.22500'
set ylabel 'mag'
set format y '%5.2f'
set xrange [-2071.30510:3130.55310]
set yrange [15.78:15.22]
plot "lightcurve.dat" using ($1)-2447477.22500:2 linecolor 2 pointtype 5 pointsize 0.3  title ""