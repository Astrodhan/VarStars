set term png size 600,350 medium
set colors classic
set output 'lightcurve.png'
set xlabel 'JD-2447057.42700'
set ylabel 'mag'
set format y '%5.2f'
set xrange [-1651.50710:3550.35110]
set yrange [15.79:15.20]
plot "lightcurve.dat" using ($1)-2447057.42700:2 linecolor 2 pointtype 5 pointsize 0.3  title ""