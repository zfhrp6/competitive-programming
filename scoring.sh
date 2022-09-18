cd tools;

rm ../scores.txt
ls in | xargs -I% -P12 cargo run --bin vis in/% out/% 2>/dev/null >> ../scores.txt

cd ../;

awk '{s += $3} END {print s}' scores.txt > total_score.txt

git --no-pager diff total_score.txt
