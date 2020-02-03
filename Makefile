help:
	poetry run gendiff -h

lint:
	@poetry run flake8 gen_diff


install:
	@poetry install



















.PHONY : help lint install
