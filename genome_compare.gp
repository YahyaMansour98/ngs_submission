set terminal png tiny size 800,800
set output "genome_compare.png"
set ytics ( \
 "NODE_1_length_9948_cov_181.191044" 1, \
 "NODE_2_length_9923_cov_198.119376" 9948, \
 "NODE_3_length_5093_cov_251.267963" 19870, \
 "NODE_4_length_5077_cov_151.740342" 24962, \
 "NODE_5_length_5053_cov_176.616046" 30038, \
 "NODE_6_length_4963_cov_244.325591" 35090, \
 "" 40057 \
)
set size 1,1
set grid
unset key
set border 10
set tics scale 0
set xlabel "MN908947.3"
set ylabel "QRY"
set format "%.0f"
set mouse format "%.0f"
set mouse mouseformat "[%.0f, %.0f]"
if(GPVAL_VERSION < 5) set mouse clipboardformat "[%.0f, %.0f]"
set xrange [1:29903]
set yrange [1:40057]
set style line 1  lt 1 lw 3 pt 6 ps 1
set style line 2  lt 3 lw 3 pt 6 ps 1
set style line 3  lt 2 lw 3 pt 6 ps 1
plot \
 "genome_compare.fplot" title "FWD" w lp ls 1, \
 "genome_compare.rplot" title "REV" w lp ls 2
