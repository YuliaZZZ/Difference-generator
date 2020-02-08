install:
	@poetry install

lint:
	@poetry run flake8 gen_diff

selfcheck:
	@poetry check

check:
	selfcheck lint

test:
	poetry run pytest --cov-report xml:./cc-test-reporter  tests/



















.PHONY : help lint install test
