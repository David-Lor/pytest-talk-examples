#!/bin/bash

pytest -s -v examples/ --ignore=examples/A_helloworld/test_A2_failing.py
