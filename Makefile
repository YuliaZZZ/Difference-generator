install:
	@poetry install

lint:
	@poetry run flake8 gen_diff



















.PHONY : help lint install
