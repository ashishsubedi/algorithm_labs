set term postscript enhanced color 'Helvetica-Bold'
set output 'ls.ps'
set autoscale
set style line 1 lt 1 lw 3 lc rgb 'red'
set xlabel 'No. of datas'
set ylabel 'Time Interval (ms)'
set key left top
set title "Linear Search"
plot 'ls_best.dat'  u 1:2  w lp smooth bezier title 'Best Case',\
'ls_avg.dat' u 1:2  w lp smooth bezier title 'Average Case',\
'ls_worst.dat' u 1:2  w lp smooth bezier title 'Worst Case'
set output
! ps2pdf 'ls.ps'
! rm -rf ls.ps