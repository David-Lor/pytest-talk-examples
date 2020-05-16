.DEFAULT_GOAL := help

test-sequential: ## run sequential tests, ignoring on-purpose failing and parallel tests
	# All sequential tests, ignoring failing and parallel tests
	pytest -s -v examples/ \
	  --ignore=examples/A_helloworld/test_A2_failing.py \
	  --ignore=examples/F_parametrize/test_F2_parametrize_failing.py \
	  --ignore=examples/H_parallelization

test-parallel: ## run parallel tests
	pytest -s -v -n auto examples/H_parallelization

test-all:
	make test-sequential
	make test-parallel

help: ## show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
