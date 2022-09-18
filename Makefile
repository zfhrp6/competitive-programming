test:
	poetry run python -m pytest -vvv tests/test_*

run:
	bash run.sh

scoring:
	bash scoring.sh
