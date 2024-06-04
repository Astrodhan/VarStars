set term png size 600,350 medium
set colors classic
set output 'phase_lc_9.png'
set xlabel 'Phase'
set ylabel 'mag'
#set title 'JDmax = 2446265.50700 + 0.1201554 x E'
set format y '%5.2f'
plot [-0.55:1.05][18.27:16.00] "phase_lc_9.dat" linecolor 3 pointtype 5 pointsize 0.3 title ""