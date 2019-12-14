#!/usr/bin/env python3
import os
from setuptools import setup, find_packages

setup(
    name="snipco",
    version="0.1a",
    author="Eron Hennessey",
    author_email="eron@abstrys.com",
    description="A command-line clipboard utility and snippet catalog",
    license="BSD",
    keywords="clipboard snip",
    packages=find_packages(),
    namespace_packages=["abstrys"],
    include_package_data=True,
    entry_points={
        'console_scripts' : ['snipco = abstrys.snipco:main'],
        },
    install_requires = ['abstrys-core']
)

