set term png size 600,350 medium
set colors classic
set output 'phase_lc_20.png'
set xlabel 'Phase'
set ylabel 'mag'
#set title 'JDmax = 2450371.33000 + 0.1339130 x E'
set format y '%5.2f'
plot [-0.55:1.05][16.24:15.54] "phase_lc_20.dat" linecolor 3 pointtype 5 pointsize 0.3 title ""