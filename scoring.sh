cd tools;

rm ../scores.txt
for f in $(ls in/); do
  cargo run --bin vis in/$f out/$f 2>/dev/null >> ../scores.txt
done

cd ../;

awk '{s += $3} END {print s}' scores.txt > total_score.txt

git --no-pager diff total_score.txt
