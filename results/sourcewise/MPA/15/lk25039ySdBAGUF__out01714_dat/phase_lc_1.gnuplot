set term png size 600,350 medium
set colors classic
set output 'phase_lc_1.png'
set xlabel 'Phase'
set ylabel 'mag'
#set title 'JDmax = 2445947.49300 + 0.9968957 x E'
set format y '%5.2f'
plot [-0.55:1.05][15.73:15.17] "phase_lc_1.dat" linecolor 3 pointtype 5 pointsize 0.3 title ""