#!/usr/bin/env python

from os import path
from setuptools import setup, find_packages

# Data
description = 'A simple set of utilities, to help with building assembly-lines in Python.'
srcDir = './src'

setup(
	name='ffffffff',
	version='0.0.1',
	package_dir={'': srcDir},
	packages=find_packages(srcDir),
	description=description,
	long_description=description,
	url='https://github.com/viswanathct/al-py',
	author='Viswanath. Ct',
	platforms='any',
	include_package_data=True,
	python_requires='>=2.7.10', #ToDo: Find and add the minimum required verion of python. This requires a scanning of the requirements and/or a test suite to figure out the answer.
	license="ISC",
	zip_safe=True,
	keywords="build assembly-line utility FP functional-programming unix-pipes builder-pattern ffffffff",
	classifiers=[
		'Development Status :: 2 - Pre-Alpha',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'Operating System :: OS Independent',
		'Natural Language :: English',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Topic :: Software Development',
		'Topic :: Utilities',
	],
	# test_suite='',
)

#ToDo: Shed any unwanted files from the package.
