install:
	python3 -m poetry install

lint:
	python3 -m poetry run flake8 gen_diff

test:
	@poetry run pytest --cov tests/














.PHONY : lint install test
