# `name` is the name of the package as used for `pip install package`
name = "python_template"
# `path` is the name of the package for `import package`
path = name.lower().replace("-", "_").replace(" ", "_")
# Your version number should follow https://python.org/dev/peps/pep-0440 and
# https://semver.org
version = "0.1"
author = "Shivam Ralli"
author_email = "shivamralli167@gmail.com"
description = (
    "Python Project Template - A global brief template that could help for creating quick pacakges"
)
url = ""  # your project homepage
license = "MIT License"  # See https://choosealicense.com
