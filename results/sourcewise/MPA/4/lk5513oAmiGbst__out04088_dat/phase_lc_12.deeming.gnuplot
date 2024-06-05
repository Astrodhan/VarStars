set term png size 600,350 medium
set colors classic
set output "phase_lc_12.deeming.png"
set xlabel "Frequency [c/d]"
set ylabel "Power"
set format y "%5.2f"
plot "deeming.periodogram" using 1:2 with lines linecolor 3 title "DFT", "deeming.periodogram" using 1:3 with lines linecolor 2 title "Window", "<echo '0.968342 48.95789989'" with impulses linecolor 1 title ""
 