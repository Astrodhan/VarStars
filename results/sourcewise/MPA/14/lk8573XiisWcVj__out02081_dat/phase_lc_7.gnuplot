set term png size 600,350 medium
set colors classic
set output 'phase_lc_7.png'
set xlabel 'Phase'
set ylabel 'mag'
#set title 'JDmax = 2446761.26400 + 0.1036399 x E'
set format y '%5.2f'
plot [-0.55:1.05][13.07:12.08] "phase_lc_7.dat" linecolor 3 pointtype 5 pointsize 0.3 title ""