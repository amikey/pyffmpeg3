#!/usr/bin/env python3
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = ['numpy', ]

test_requirements = ['pytest', ]

setup(
    author="Mark Harfouche",
    author_email='mark.harfouche@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python FFmpeg bindings for fast video encoding and decoding",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pyffmpeg',
    name='pyffmpeg',
    packages=find_packages(include=['pyffmpeg']),
    tests_require=test_requirements,
    url='https://github.com/hmaarrfk/pyffmpeg',
    version='0.0.1',
    zip_safe=False,
)