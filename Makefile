.DEFAULT_GOAL := help

test-sequential: ## run sequential tests, ignoring on-purpose failing and parallel tests
	# All sequential tests, ignoring failing and parallel tests
	pytest -s -v examples/ \
	  --ignore=examples/A_helloworld/test_A2_failing.py \
	  --ignore=examples/F_parametrize/test_F2_parametrize_failing.py \
	  --ignore=examples/H_parallelization \
	  -k "not random_number_fixture_fails and not expect_zerodivisionerror_not_raised and not expect_zerodivisionerror_raised_other"

test-parallel: ## run parallel tests
	pytest -s -v -n auto examples/H_parallelization

test-all: ## run all tests
	make test-sequential
	make test-parallel

install-requirements: ## pip install requirements
	pip install -r requirements.txt

run-jupyter: ## run the jupyter notebook server
	jupyter notebook

help: ## show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
