rm -f scores.txt
for i in $(seq 0 99);
do cargo run -r --bin tester python ../main.py < "in/${(l:4::0:)i}.txt" > out.txt 2>>scores.txt
done
rm -f out.txt
cat scores.txt | awk '/^Score.*/{sum+=$3} END {print sum}'
