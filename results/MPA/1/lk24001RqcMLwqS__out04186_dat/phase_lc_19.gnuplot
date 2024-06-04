set term png size 600,350 medium
set colors classic
set output 'phase_lc_19.png'
set xlabel 'Phase'
set ylabel 'mag'
#set title 'JDmax = 2445918.53400 + 0.1314017 x E'
set format y '%5.2f'
plot [-0.55:1.05][16.71:15.77] "phase_lc_19.dat" linecolor 3 pointtype 5 pointsize 0.3 title ""