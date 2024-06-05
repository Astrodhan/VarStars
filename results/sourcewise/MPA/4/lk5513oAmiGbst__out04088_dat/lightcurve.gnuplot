set term png size 600,350 medium
set colors classic
set output 'lightcurve.png'
set xlabel 'JD-2446709.42200'
set ylabel 'mag'
set format y '%5.2f'
set xrange [-1301.46090:3898.25890]
set yrange [16.88:16.10]
plot "lightcurve.dat" using ($1)-2446709.42200:2 linecolor 2 pointtype 5 pointsize 0.3  title ""