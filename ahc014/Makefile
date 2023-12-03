.PHONY: profile test run all

all: test run profile

test:
	poetry run python -m pytest -vvv tests/test_*

run: solver.py
	bash run.sh && bash scoring.sh

profile: profile.webp profile.prof

profile.webp: profile.prof
profile.prof: solver.py
	bash profile.sh
