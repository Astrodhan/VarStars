set term png size 600,350 medium
set colors classic
set output 'phase_lc_14.png'
set xlabel 'Phase'
set ylabel 'mag'
#set title 'JDmax = 2446709.42200 + 1.8635647 x E'
set format y '%5.2f'
plot [-0.55:1.05][17.30:15.98] "phase_lc_14.dat" linecolor 3 pointtype 5 pointsize 0.3 title ""