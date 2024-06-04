set term png size 600,350 medium
set colors classic
set output 'lightcurve.png'
set xlabel 'JD-2446768.21900'
set ylabel 'mag'
set format y '%5.2f'
set xrange [-1362.29910:3839.55910]
set yrange [14.44:13.96]
plot "lightcurve.dat" using ($1)-2446768.21900:2 linecolor 2 pointtype 5 pointsize 0.3  title ""