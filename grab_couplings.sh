for i in `seq 1 5000`;
do
	grep "      $i  " couplings.log | grep "   0   " > $i.dat
	awk '{ total += $3 } END { print total/NR }' $i.dat >> avg_coups.dat
done


