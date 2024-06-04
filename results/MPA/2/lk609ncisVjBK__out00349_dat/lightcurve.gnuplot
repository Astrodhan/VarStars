set term png size 600,350 medium
set colors classic
set output 'lightcurve.png'
set xlabel 'JD-2450365.43900'
set ylabel 'mag'
set format y '%5.2f'
set xrange [-4959.51910:242.33910]
set yrange [17.26:15.93]
plot "lightcurve.dat" using ($1)-2450365.43900:2 linecolor 2 pointtype 5 pointsize 0.3  title ""