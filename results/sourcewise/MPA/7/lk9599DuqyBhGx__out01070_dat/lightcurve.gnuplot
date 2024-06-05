set term png size 600,350 medium
set colors classic
set output 'lightcurve.png'
set xlabel 'JD-2445933.40800'
set ylabel 'mag'
set format y '%5.2f'
set xrange [-527.48810:4674.37010]
set yrange [16.43:15.70]
plot "lightcurve.dat" using ($1)-2445933.40800:2 linecolor 2 pointtype 5 pointsize 0.3  title ""