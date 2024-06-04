set term png size 600,350 medium
set colors classic
set output 'phase_lc_5.png'
set xlabel 'Phase'
set ylabel 'mag'
#set title 'JDmax = 2446084.21800 + 0.5092962 x E'
set format y '%5.2f'
plot [-0.55:1.05][17.59:16.11] "phase_lc_5.dat" linecolor 3 pointtype 5 pointsize 0.3 title ""