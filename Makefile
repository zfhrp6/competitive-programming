test:
	poetry run python -m pytest -vvv tests/test_*

run:
	bash run.sh && sleep 10 && bash scoring.sh

scoring:
	bash scoring.sh
