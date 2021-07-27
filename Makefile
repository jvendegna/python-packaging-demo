.PHONY: lint, test, clean, setup, report, all

lint:
	poetry run flake8 --ignore=E251,E226 --max-line-length=100

test:
	poetry run coverage run -m pytest

setup:
	poetry run python op1fun/main.py get-user

report: test
	poetry run coverage report
	poetry run coverage html

clean:
	poetry run black -l 88 .


all: setup clean lint report