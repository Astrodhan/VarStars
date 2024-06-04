set term png size 600,350 medium
set colors classic
set output 'phase_lc_13.png'
set xlabel 'Phase'
set ylabel 'mag'
#set title 'JDmax = 2447477.22500 + 27.0709258 x E'
set format y '%5.2f'
plot [-0.55:1.05][15.78:15.22] "phase_lc_13.dat" linecolor 3 pointtype 5 pointsize 0.3 title ""