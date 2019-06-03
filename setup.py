# Copyright (C) 2014 Stefan C. Mueller

import os.path
from setuptools import setup, find_packages

if os.path.exists('README.rst'):
    with open('README.rst') as f:
        long_description = f.read()
else:
    long_description = None
    
setup(
    name = 'pydron_dataflow',
    version = '0.2.5',
    description='Dataflow framework to define and traverse directional graphs.',
    long_description=long_description,
    author='Ivo Nussbaumer',
    author_email='ivo.nussbaumer@fhnw.ch',
    url='https://github.com/i4Ds/pydron-dataflow',
    packages = find_packages(),
    install_requires = ['astor>=0.4',
                        'frozendict>=0.4',
                        'twisted_sshtools>=2.2.4',
                        'sortedcontainers>=0.9.5']
)
