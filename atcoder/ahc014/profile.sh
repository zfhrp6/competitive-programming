cat tools/in/0000.txt | poetry run python -m cProfile -o profile.prof solver.py - >/dev/null

poetry run gprof2dot -f pstats profile.prof | dot -Twebp -Gdpi=144 -o profile.webp
