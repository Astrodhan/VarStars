set term png size 600,350 medium
set colors classic
set output 'lightcurve.png'
set xlabel 'JD-2446709.42200'
set ylabel 'mag'
set format y '%5.2f'
set xrange [-1303.50210:3898.35610]
set yrange [17.30:15.98]
plot "lightcurve.dat" using ($1)-2446709.42200:2 linecolor 2 pointtype 5 pointsize 0.3  title ""