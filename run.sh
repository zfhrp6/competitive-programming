ls tools/in | xargs -I% -P12 bash -c 'echo %; cat tools/in/% | poetry run python solver.py - > tools/out/%'
