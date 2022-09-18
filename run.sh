for f in $(ls tools/in); do
  echo $f;
  cat tools/in/$f | poetry run python solver.py - > tools/out/$f &
done
