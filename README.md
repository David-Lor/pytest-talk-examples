# pyTest talk - examples + notebook (ES)

![Test](https://github.com/David-Lor/pytest-talk-examples/workflows/Test/badge.svg)

## Requirements

- Python >= 3.6 (virtual env recommended)
- requirements listed in [requirements.txt](requirements.txt)

## Running tests

Run ALL tests with:

```bash
pytest -sv
```

Run individual tests with (example):

```bash
# Only A1
pytest -sv examples/A_helloworld/test_A1_helloworld.py

# All modules in B_before_after package
pytest -sv examples/B_before_after
```
