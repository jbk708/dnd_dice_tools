## Requirements:
- Python ^3.9
- Poetry Package Manager --> [Link to Install Page](https://python-poetry.org/docs/#installing-with-the-official-installer)

## Installation:

1. Clone git repo into directory of choice
2. Open main repo directory
3. run `poetry install`
4. Run your module of choice with `poetry run {module}`

## Modules
single-die-odds: Gives the average number of rolls needed to hit a target number, and the odds of hitting a number or set of numbers you're trying to avoid.

Args:
```
 --target TARGET 
 --max_num MAX_NUM 
 [--forbidden_numbers [FORBIDDEN_NUMBERS ...]]
```
## Code Testing, Formatting, and Linting Standards

To run tests run [pytest](https://docs.pytest.org/en/7.4.x/) from the root folder:


For code formatting, simply run [yapf](https://github.com/google/yapf) from the root folder:

```sh
poetry run yapf --in-place --recursive ./dnd_odds ./tests
```

For linting, simply run [pylint](https://pylint.pycqa.org/en/latest/) from the root folder:
```sh
poetry run pylint ./dnd_odds ./tests
