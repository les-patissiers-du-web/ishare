#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import ishare


setup(
    name='ishare',
    version=ishare.__version__,
    description="A simple command line tool for sharing files",
    author='Nicolas RAMY',
    author_email='nicolas.ramy@darkelda.com',
    url='https://github.com/nicolasramy/ishare',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'ishare=ishare.__main__:main'
        ],
    },
    install_requires=[
        'paramiko',
        'progressbar2',
        'python-slugify',
    ],
    tests_require=[
        'coverage>=4.5.1',
    ],
    test_suite='tests',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
)
