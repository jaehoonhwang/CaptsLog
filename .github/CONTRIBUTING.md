# Contributing to CaptsLog

We are test-driven, though we gonna do some switching between test first and test second method.

## Source Code

Every source code should be `source/` (It will be change to `captslog/` later)

Create different directories for UI, DB, and call them `tests` files.

### Example of test directory

File directories should look like as this

**Database**
```
source/DB/
    - source/DB/tests
```

**UI**
```
source/UI/
    - source/UI/tests
```

## Testing Environment

We are going to use `py.test` module.

Read documentations for individual file testing, but in general, it should go something like this

```
pytest /source/path/to/tests/
```

It should be very short and we'll talk about UI testing later

## Travis-CI

If you have any problem with Travis-CI, email me or create github issue.

Every single tests will be tested through following command:

```bash
py.test source/tests/tests.py --pep8 source/tests/ -v --cov source/tests/ --cov-report term-missing
```

## Coveralls

We are shooting for that **85%+** coverage
