set term png size 600,350 medium
set colors classic
set output "phase_lc_16.deeming.png"
set xlabel "Frequency [c/d]"
set ylabel "Power"
set format y "%5.2f"
plot "deeming.periodogram" using 1:2 with lines linecolor 3 title "DFT", "deeming.periodogram" using 1:3 with lines linecolor 2 title "Window", "<echo '9.081483 10.40107632'" with impulses linecolor 1 title ""
 
