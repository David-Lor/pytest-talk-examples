# pyTest talk - slideshow (ES) + examples

![Test](https://github.com/David-Lor/pytest-talk-examples/workflows/Test/badge.svg)

## Requirements

Listed on [requirements.txt](requirements.txt); install everything with:

```bash
pip install --user -r requirements.txt
```

Tests C_fixtures, D_class_inherit require a running MongoDB server on localhost!

## Running tests

Run ALL tests with:

```bash
pytest -s -v
```

Run individual tests with:

```bash
pytest -s -v examples/1_before_after
```

## Requirements

- Python >= 3.6
- requirements listed in [requirements.txt](requirements.txt)
