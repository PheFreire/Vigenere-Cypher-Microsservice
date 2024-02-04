.DEFAULT_GOAL := help
.SILENT:
.PHONY: help

help:  ## Display this help
	awk 'BEGIN {FS = ":.*## "; printf "Usage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Format

format-black: ## run black (code formatter)
	poetry run black .

format-isort: ## run isort (imports formatter)
	poetry run isort .

format: format-black format-isort ## run all formatters

##@ Check

check-bandit: ## run bandit (check for common security issues)
	poetry run bandit -r ./src

check-black: ## run black in check mode
	poetry run black . --check

check-isort: ## run isort in check mode
	poetry run isort . --check

check-flake8: ## run flake8 (pep8 linter)
	poetry run flake8 ./src

check-mypy: ## run mypy (static-type checker)
	poetry run mypy ./src

check-mypy-report: ## run mypy & create report
	poetry run mypy ./src --html-report ./mypy_html

check: check-bandit check-black check-isort check-flake8 check-mypy ## run all checks

##@ Test

test: ## run tests
	poetry run pytest | tee tests.log

##@ Run Code

run_main: ## run tests
	cd ./src && poetry run python main.py

run_api: ## run tests
	cd ./src && poetry run uvicorn main:app --reload --host=0.0.0.0 --port=8000
