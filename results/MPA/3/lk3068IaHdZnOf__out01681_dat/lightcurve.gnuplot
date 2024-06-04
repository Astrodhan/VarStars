set term png size 600,350 medium
set colors classic
set output 'lightcurve.png'
set xlabel 'JD-2446084.21800'
set ylabel 'mag'
set format y '%5.2f'
set xrange [-678.29810:4523.56010]
set yrange [17.59:16.11]
plot "lightcurve.dat" using ($1)-2446084.21800:2 linecolor 2 pointtype 5 pointsize 0.3  title ""