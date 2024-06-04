set term png size 600,350 medium
set colors classic
set output 'phase_lc_18.png'
set xlabel 'Phase'
set ylabel 'mag'
#set title 'JDmax = 2450365.43900 + 0.7500941 x E'
set format y '%5.2f'
plot [-0.55:1.05][17.26:15.93] "phase_lc_18.dat" linecolor 3 pointtype 5 pointsize 0.3 title ""