# Dynamic Python Template

Welcome to dynamic_python_template!
This project aims to provide a simple and easy-to-use template for Python projects. One of the key features of python_template is the ability to dynamically import modules and packages regardless of their location within the project directory. This means that you can structure your project however you like and still be able to import modules and packages as needed. No more worrying about relative or absolute import paths! Simply import what you need and get to work.

## Features

- Dynamic Python imports if function names are the same. 
- Init files which follow a syntax for importing based on full customization as regular python imports.
- Tests in the same folder as the development code
- Easy to modify and make your own code structure
- Coverage tracker with a simple pytest coverage.

## Setup

To set this repository up, the first step is to set the new variables in the
`__meta__.py` file

To fill in these variables, simply replace the values in the "" with your desired values. For example:

```python
name = "my_project"
path = "my_project"
version = "1.0.0"
author = "John Smith"
author_email = "john@example.com"
description = "This is my amazing project"
url = "https://www.example.com/my_project"
license = "MIT License"
```

Make sure to use your own information for `name`, `author`, `author_email`, `description`, `url`, and `license`. \
The path variable should be set to the lowercase, hyphen-separated version of name, with any spaces replaced with underscores. The version variable should follow the semantic versioning format, with major, minor, and patch versions separated by dots.

In `setup.py`
In line 52, replace `python_template` in `exec(read("python_template/__meta__.py"), meta)` to your repository/package name.

## Modify requirements.txt
Add all your requirements in this file as all the dependencies are installed from this file.

## Installation after setup for your repository

```bash
#For installing it in dev mode
pip install -e .
# For prod mode
pip install .
```

## Running Tests and coverage report

To run tests, run the following command

```bash
  pytest --cov=python_template
```

## Roadmap

- Decorator Support, if needed

- CI/CD template addition

## Authors

- [@sralli](https://www.github.com/sralli)

## License

[MIT](https://choosealicense.com/licenses/mit/)
