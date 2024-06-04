set term png size 600,350 medium
set colors classic
set output 'lightcurve.png'
set xlabel 'JD-2446265.50700'
set ylabel 'mag'
set format y '%5.2f'
set xrange [-733.58275:1696.17975]
set yrange [18.27:16.00]
plot "lightcurve.dat" using ($1)-2446265.50700:2 linecolor 2 pointtype 5 pointsize 0.3  title ""