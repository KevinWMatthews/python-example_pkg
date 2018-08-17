# Example Package

A sample Python package.
Created following the tutorial at [packaging.python.org](https://packaging.python.org/tutorials/packaging-projects/).

## Setup

### Virtualenv

I've been running this from within an virtual environment using `virtualenv`.
This may be out of fashion, but this is what I know; learn one thing at a time.

Install your system's python3 into the virtual environment.

```
$ virtualenv --python=python3 venv
$ source venv/bin/activate
```

When finished, deactivate the venv using:
```
$ deactivate
```

## Generate Distribution Files

Python recommends generating both `sdist` and `bdist_wheel` unless you have
a good reason to do otherwise.
I don't know what either of these really are, so just trust them.

```
$ python setup.py sdist bdist_wheel
```

This generates several directories:

  * `build` for building the python package
  * `dist` contains a `wheel` and `.tar.gz` for distribution
  * `example_pkg.egg-info` looks cool...

## setup.py Commands

`setup.py` features several useful commands:

  * [Build](#build) builds the python package in `build/`
  * [Clean](#clean) removes what was built
  * [Install](#install) installs the entire package to system or into a venv
  * [Uninstall](#uninstall) using `pip`
  * [sdist](#source-distribution) creates a tarball of the source distribution
  * [bdidt_wheel](#binary-distribution) creates a binary distribution

### Build

Builds the python package. Not entirely sure what this means.
Puts build results in the `build/` directory by default.
Override this with the `--build-base (-b)` option.
This can be cleaned using `setup.py`'s `clean` target; see [Clean](#clean).

### Clean

`clean` has several subcommands

```
$ python setup.py clean --all
```

See the help for more details.

### Source Distribution

The source distribution is installed to `dist/` by default.
Change this using the `--dist-dir (-d)` option.
I don't know how to clean this folder; I think it must be deleted manually or
installed out-of-tree.

### Binary Distribution

`bdist_wheel` isn't listed in the help but it seems to work.

The source distribution is installed to `dist/` by default.
Change this using the `--dist-dir (-d)` option.
It also creates `build` and `.egg-info` directories during the build process.

I don't know how to clean this folder; I think it must be deleted manually or
installed out-of-tree.

### .egg-info

Go read about this. It must be important.

## Install package

### From current directory

The package can be installed directly from the development directory.
In our case, install to the virtual environment:

```
$ cd example_pkg
$ source venv/bin/activate
$ pip install .
```

You may then use the package as follows:
```
$ python
>>> import example_pkg
>>> example_pkg.example_function()
>>> exit()
```

Uninstall using:
```
$ pip uninstall example_pkg
```


### From distribution Files

TODO


## Tests

See [readthedocs](https://python-packaging.readthedocs.io/en/latest/testing.html)
for a basic introduction.

The most straightforward way is to follow the guide's recommendation and use `Nose`:

```
$ nosetests
```
Wild. It just worked.

I've integrated `nose` into `setup.py` so one can also run:

```
$ setup.py --test
```

This seems to both build the package and run the tests.

It is possible to load unit tests manually in the test file.
I think you might need a `TestLoader` and `Runner` from `UnitTest`.
This sounds like too much work.


## Links

  * [Further reading](https://packaging.python.org/guides/distributing-packages-using-setuptools/)
  * [Sample Project](https://github.com/pypa/sampleproject/blob/master/setup.cfg)
  * [What is egg-info](https://stackoverflow.com/questions/3779915/why-does-python-setup-py-sdist-create-unwanted-project-egg-info-in-project-r)
  * [Minimal package](http://python-packaging.readthedocs.io/en/latest/minimal.html)
