set term png size 600,350 medium
set colors classic
set output 'lightcurve.png'
set xlabel 'JD-2446761.26400'
set ylabel 'mag'
set format y '%5.2f'
set xrange [-1355.34410:3846.51410]
set yrange [13.07:12.08]
plot "lightcurve.dat" using ($1)-2446761.26400:2 linecolor 2 pointtype 5 pointsize 0.3  title ""