# chromotools
Toolkit for chromosome segmentation and manipulation in microscopy images, designed for advanced genetic analysis.

[![Powered by daftar.digital](https://img.shields.io/badge/powered%20by-daftar.digital-orange.svg?style=flat&logo=gravatar)](https://daftar.digital)

[![Reference](https://img.shields.io/badge/Reference-Article%20PDF-blue)](https://raw.githubusercontent.com/daftar/chromotools/main/specs/wvc-2020/_WVC_2020__Rodrigo-J-R-Santos.pdf)


[![codecov](https://codecov.io/github/RodrigoSantosRodrigues/chromotools/graph/badge.svg?token=IGAGLZ49LI)](https://codecov.io/github/RodrigoSantosRodrigues/chromotools)

![alt text](https://codecov.io/github/RodrigoSantosRodrigues/chromotools/graphs/sunburst.svg?token=IGAGLZ49LI)


It provides:

----------------------

Guide

[Guide](https://opensource.guide/how-to-contribute/)


## start project

## Prerequisites
  - Install [Python](https://www.python.org/downloads/), [Pipenv](https://docs.pipenv.org/)

# Instalation dependency:

pip install -r requirements.txt


1. Tests
Execute tests:

python -m unittest discover tests

pytest --html=test-reports/report.html


1. Publish in PyPI
pip install twine wheel


Generate distribution:
python setup.py sdist bdist_wheel


Publish in PyPI:
twine upload dist/*


### Commit Structure
A conventional commit typically follows the following structure:


- **Type:** Indicates the nature of the commit. Common types include `feat` (for new features), `fix` (for bug fixes), `docs` (for documentation changes), `style` (for code style changes that do not affect behavior), `refactor` (for code refactoring), `test` (for adding or modifying tests), among others.

- **Scope (optional):** Can be used to specify the part of the code being changed by the commit.

- **Description:** A concise and clear description of what was changed in the commit.

### Examples of Commit Messages

Here are some examples of commit messages following the Conventional Commits standard:

- `feat: Add support for OAuth authentication`
- `fix: Fix logic error in tax calculation`
- `docs: Update documentation for endpoint /api/users`
- `style: Adjust indentation in views.py file`
- `refactor: Extract email validation function to util.py`
- `test: Add unit tests for login function`

### Benefits of the Conventional Commit Standard

- **Clarity:** Facilitates quick understanding of changes introduced by each commit.
- **Automation:** Automation tools such as changelog generators and continuous integration can use commit messages to automate tasks.
- **Clean History:** Helps maintain a cleaner and organized commit history.

### Supporting Tools

There are tools that help implement and maintain the Conventional Commits standard, such as `commitizen` and `git-cz`, which guide developers in creating commit messages in the correct format.

Following these guidelines not only improves team collaboration but also facilitates the maintenance and evolution of software projects over time.

## Linter
Before commits and pushes
`pre-commit run --all-files`

## for update docs
  - `sphinx-apidoc -o docs/source/ ../chromotools`
  - `make html`


## utils

https://peps.python.org/pep-0008/


## VERSIONS

### 0.1.3
- **Description:** Toolkit for chromosome segmentation, designed for advanced genetic analysis.
- **Author:** contato@daftar.digital
- **Published:** Sun, 07 Jul 2024 02:24:20 GMT
- **Link:** [0.1.3](https://pypi.org/project/chromotools/0.1.3/)

### 0.1.2
- **Description:** Toolkit for chromosome segmentation, designed for advanced genetic analysis.
- **Author:** contato@daftar.digital
- **Published:** Sun, 07 Jul 2024 02:24:20 GMT
- **Link:** [0.1.2](https://pypi.org/project/chromotools/0.1.2/)

### 0.1.1
- **Description:** Toolkit for chromosome segmentation, designed for advanced genetic analysis.
- **Author:** contato@daftar.digital
- **Published:** Sun, 07 Jul 2024 02:13:06 GMT
- **Link:** [0.1.1](https://pypi.org/project/chromotools/0.1.1/)

### 0.1
- **Description:** Toolkit for chromosome segmentation, designed for advanced genetic analysis.
- **Author:** contato@daftar.digital
- **Published:** Sat, 06 Jul 2024 20:26:26 GMT
- **Link:** [0.1](https://pypi.org/project/chromotools/0.1/)

- **Website:** https://daftar.digital
- **Documentation:** https://daftar.digital/doc
- **Source code:** https://github.com/daftar/chromotools
- **Contributing:** https://daftar/chromotools/dev/index.html
- **Bug reports:** https://github.com/daftar/chromotools/issues
