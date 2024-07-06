# chromotools
Toolkit for chromosome segmentation and manipulation in microscopy images, designed for advanced genetic analysis.

<h1 align="center">
<img src="https://raw.githubusercontent.com/daftar/chromotools/main/branding/logo/logo_daftar.png" width="300">
</h1><br>



[![Powered by daftar.digital](https://img.shields.io/badge/powered%20by-daftar.digital-orange.svg?style=flat&logo=gravatar)](https://daftar.digital)

[![Reference](https://img.shields.io/badge/Reference-Article%20PDF-blue)](https://raw.githubusercontent.com/daftar/chromotools/main/specs/wvc-2020/_WVC_2020__Rodrigo-J-R-Santos.pdf)


[![Coverage Status](https://img.shields.io/codecov/c/github/daftar/chromotools?style=flat-square)](https://codecov.io/gh/daftar/chromotools)



- **Website:** https://daftar.digital
- **Documentation:** https://daftar.digital/doc
- **Source code:** https://github.com/daftar/chromotools
- **Contributing:** https://daftar/chromotools/dev/index.html
- **Bug reports:** https://github.com/daftar/chromotools/issues
It provides:


----------------------

Call for Contributions
----------------------


If you are new to contributing to open source, [this
guide](https://opensource.guide/how-to-contribute/) helps explain why, what,
and how to successfully get involved.


## start project

## Prerequisites
  - Install [Python](https://www.python.org/downloads/), [Pipenv](https://docs.pipenv.org/), [Docker](https://www.docker.com/) and [Postgres](https://www.postgresql.org/) on your machine




# Instalar Dependências:

pip install -r requirements.txt  # Se houver um arquivo de requisitos


1. Rodar Testes
Executar Testes:

python -m unittest discover tests

pytest --html=test-reports/report.html


1. Publicar no PyPI
Instalar Ferramentas Necessárias:

pip install twine wheel


Gerar Distribuição:

python setup.py sdist bdist_wheel


Publicar no PyPI:

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
