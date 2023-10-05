## Installation:

1. Clone git repo into directory of choice
2. Open main repo directory
3. run `poetry install`
4. Run your module of choice with `poetry run {module}`

## Modules


## Code Formatting and Linting Standards

For code formatting, simply run [yapf](https://github.com/google/yapf) from the root folder:

```sh
poetry run yapf --in-place --recursive ./dnd_odds ./tests
```

For linting, simply run [pylint](https://pylint.pycqa.org/en/latest/) from the root folder:
```sh
poetry run pylint ./dnd_odds ./tests