#!/usr/bin/env python
"""
# Author: Xiong Lei
# Created Time : Thu 18 Oct 2018 02:42:37 PM CST

# File Name: setup.py
# Description:

"""

from distutils.core import setup

install_requires = [
	'torch>=0.4.0',
	'vsidom>=0.1.6.5',
	'scikit-learn>=0.19.1',
	'pandas>=0.22.0',
	'numpy>=1.14.2',
	'scipy>=0.19.1'
]

setup(name='SCALE',
	  version='0.8',
	  description='Single-Cell ATAC-seq Analysis via Latent feature Extraciton',
	  author='Xiong Lei',
	  author_email='',
	  url='',
	  packages=['scale', ],
	  scripts=['SCALE.py','chromVAR.R'],
	 )