set term png size 600,350 medium
set colors classic
set output "phase_lc_9.lk.png"
set xlabel "Frequency [c/d]"
set ylabel "1/theta"
set format y "%5.2f"
plot [] "lk.periodogram" using 1:2 with lines linecolor 3 title "", "<echo '5.219642  0.90'" with impulses linecolor 1 title ""
 
