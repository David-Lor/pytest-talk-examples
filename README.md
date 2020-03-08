# pyTest talk - examples + notebook (ES)

![Test](https://github.com/David-Lor/pytest-talk-examples/workflows/Test/badge.svg)

## Requirements

- Python >= 3.6
- requirements listed in [requirements.txt](requirements.txt)
- Tests C_fixtures, D_class_inherit require a running MongoDB server on localhost

## Running tests

Run ALL tests with:

```bash
pytest -s -v
```

Run individual tests with:

```bash
pytest -s -v examples/1_before_after
```
