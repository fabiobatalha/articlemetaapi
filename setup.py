#!/usr/bin/env python
from setuptools import setup, find_packages

install_requires = [
    'thriftpy>=0.3.1',
    'requests>=2.8.1',
    'xylose'
]

tests_require = []

setup(
    name="articlemetaapi",
    version="1.2.0",
    description="Library that implements the endpoints of the ArticleMeta API",
    author="SciELO",
    author_email="scielo-dev@googlegroups.com",
    maintainer="Fabio Batalha",
    maintainer_email="fabio.batalha@scielo.org",
    url="http://github.com/scieloorg/processing",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ],
    dependency_links=[
        "git+https://git@github.com/scieloorg/xylose.git@1.16.5#egg=xylose"
    ],
    tests_require=tests_require,
    test_suite='tests',
    install_requires=install_requires
)
