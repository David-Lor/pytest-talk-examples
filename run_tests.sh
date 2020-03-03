#!/bin/bash

pytest -s -v examples/ \
  --ignore=examples/A_helloworld/test_A2_failing.py \
  --ignore=examples/F_parametrize/test_F2_parametrize_failing.py \
  --ignore=examples/H_parallelization
pytest -s -v -n auto examples/H_parallelization
