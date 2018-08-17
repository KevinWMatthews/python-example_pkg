import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example_pkg",
    version="0.0.1",
    author="Kevin Matthews",
    author_email="please_dont_email_me@not_mail.com",
    description="An example of a python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KevinWMatthews/python-example_pkg",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    test_suite='nose.collector',
    tests_require=['nose'],
)
