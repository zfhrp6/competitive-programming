test:
	poetry run python -m pytest -vvv tests/test_*

run:
	bash run.sh && bash scoring.sh
