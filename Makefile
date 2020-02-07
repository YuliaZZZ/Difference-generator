install:
	@poetry install

test:
	poetry run pytest --cov  tests/

lint:
	@poetry run flake8 gen_diff



















.PHONY : help lint install test
