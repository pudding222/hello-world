#!/usr/bin/env python
# Always prefer setuptools over distutils
from setuptools import setup
from codecs import open
from os import path
import re

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


with open(path.join(here, "helloworld", '__init__.py'), 'r') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')



setup(
    name='helloworld',
    version=version,
    description="Python HelloWorld",
    long_description=long_description,
    url='https://github.com/pudding222/hello-world',
    author='Dan',
    author_email='pud_2@hotmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Operating System :: OS Independent',
    ],
    keywords='helloworld python',
    packages=["helloworld", "helloworld.test"],
    include_package_data=True,
    install_requires=['flask >= 0.10.1'],
    test_suite="helloworld.test.all",
    extras_require={
        'test': ['pep8'],
    },
)
