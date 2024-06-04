set term png size 600,350 medium
set colors classic
set output 'lightcurve.png'
set xlabel 'JD-2450371.33000'
set ylabel 'mag'
set format y '%5.2f'
set xrange [-4965.41010:236.44810]
set yrange [16.24:15.54]
plot "lightcurve.dat" using ($1)-2450371.33000:2 linecolor 2 pointtype 5 pointsize 0.3  title ""