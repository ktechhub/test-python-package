# test-python-package
Package Your Python Code


## Structure your project

```console
├── app.py
├── build
│   ├── bdist.linux-x86_64
│   └── lib
│       └── package
│           ├── api.py
│           ├── __init__.py
│           └── __version__.py
├── dist
│   ├── ktechhub-0.0.1-py3-none-any.whl
│   └── ktechhub-0.0.1.tar.gz
├── image.png
├── ktechhub.egg-info
│   ├── dependency_links.txt
│   ├── PKG-INFO
│   ├── requires.txt
│   ├── SOURCES.txt
│   └── top_level.txt
├── LICENSE
├── package
│   ├── api.py
│   ├── __init__.py
│   └── __version__.py
├── README.md
├── requirements.txt
├── setup.py
└── tests
    ├── configtest.py
    └── test_app.py
```

## Init file
```console
touch package/__init__.py
```

## Setup file
Now that your project structure is ready, you need to add basic information about the project -- like its name, the version, and what other packages it requires.

That information is provided in the form of `setup.py`. We'll base our setup.py file on [setup.py for humans](https://github.com/navdeep-G/setup.py)

Read more about setup.py from stackoverflow [https://stackoverflow.com/questions/1471994/what-is-setup-py](https://stackoverflow.com/questions/1471994/what-is-setup-py)

Add this file to the project root.

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os

from setuptools import find_packages, setup

# Package meta-data.
NAME = "ktechhub"
DESCRIPTION = "ktechhub: A demo package."
EMAIL = "info@ktechhub.com"
AUTHOR = "KtechHub"
REQUIRES_PYTHON = ">=3.8.0"
VERSION = "0.0.1" #package version

# Which packages are required for this module to be executed?
REQUIRED = [
    "requests==2.27.1",
    #add more here
]

# The rest you shouldn't have to touch too much :)
here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION


# Where the magic happens:
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(exclude=["test_*"]),
    install_requires=REQUIRED,
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
    setup_requires=["wheel"],
)
```

The only thing that you will need to change is mostly the Package meta-data part.

You shouldn't have to touch the rest. But make sure to take a look at the bottom function called `setup()`.


## Building
you need to build the archives and wheels:

```console
python setup.py sdist bdist_wheel
```

Run it and you will see a dist folder created that includes an archive and a wheel file.

You can distribute the wheel file for installation:

```console
pip install ktechhub-0.0.1-py3-none-any.whl
```

## Wanna publish to PyPi?
To do that, you will need an account on PyPI. So, go ahead and register

You will also need a package called twine, which is a utility for publishing Python packages on PyPI:

```console
pip install twine
```

You can run the following command to see if build were created correctly:

```console
twine check dist/*
```

If all the checks passed, you can upload the framework to PyPI:

```console
twine upload dist/*
```
You will be prompted for your username and password.


Once uploaded, navigate to https://pypi.org/project/PACKAGE_NAME/


You can now easily install your package:

```console
pip install <PACKAGE_NAME>
```
