from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-haversine",
    description="Datasette plugin that adds a custom SQL function for haversine distances",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-haversine",
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_haversine"],
    entry_points={"datasette": ["haversine = datasette_haversine"]},
    install_requires=["datasette", "haversine"],
    extras_require={"test": ["pytest"]},
    tests_require=["datasette-haversine[test]"],
)
