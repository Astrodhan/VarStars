set term png size 600,350 medium
set colors classic
set output 'phase_lc_16.png'
set xlabel 'Phase'
set ylabel 'mag'
#set title 'JDmax = 2446709.42200 + 0.2194900 x E'
set format y '%5.2f'
plot [-0.55:1.05][16.88:16.10] "phase_lc_16.dat" linecolor 3 pointtype 5 pointsize 0.3 title ""