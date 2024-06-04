set term png size 600,350 medium
set colors classic
set output 'lightcurve.png'
set xlabel 'JD-2445918.53400'
set ylabel 'mag'
set format y '%5.2f'
set xrange [-512.61410:4689.24410]
set yrange [16.71:15.77]
plot "lightcurve.dat" using ($1)-2445918.53400:2 linecolor 2 pointtype 5 pointsize 0.3  title ""