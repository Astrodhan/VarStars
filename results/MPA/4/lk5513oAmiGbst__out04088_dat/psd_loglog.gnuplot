set term png size 600,350 medium
set colors classic
set output "psd_loglog.png"
set xlabel "Frequency [c/d]"
set ylabel "Power"
set logscale
#set format y "%5.2f"
plot "deeming.periodogram" using 1:2 with lines linecolor 3 title "PSD"