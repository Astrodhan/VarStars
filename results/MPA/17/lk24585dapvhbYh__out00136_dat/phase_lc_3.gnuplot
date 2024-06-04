set term png size 600,350 medium
set colors classic
set output 'phase_lc_3.png'
set xlabel 'Phase'
set ylabel 'mag'
#set title 'JDmax = 2447765.43500 + 2.0682994 x E'
set format y '%5.2f'
plot [-0.55:1.05][15.16:14.76] "phase_lc_3.dat" linecolor 3 pointtype 5 pointsize 0.3 title ""