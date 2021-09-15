#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
from dataintodatabase.__version__ import version
with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['cchardet','rich']

test_requirements = [ ]

setup(
    author="dataintodatabase",
    author_email='qin__xuan@yeah.net',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="生成pg数据库的入库脚本文件",
    entry_points={
        'console_scripts': [
            'did=dataintodatabase.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='dataintodatabase',
    name='dataintodatabase',
    packages=find_packages(include=['dataintodatabase', 'dataintodatabase.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/qinxian1989/dataintodatabase',
    version=version,
    zip_safe=False,
)
