#!/usr/bin/env python3
from setuptools import setup, find_packages


setup(
    name='Misspeller',
    description='Module that makes typos',
    long_description=open('readme.markdown').read(),
    author='Igor Trofimov',
    author_email='mister.larpy@gmail.com',
    url='https://github.com/LARPY/misspeller',
    keywords='misspeller misspelling typo error',
    version='0.1.dev',
    python_requires='>=3',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
      'Development Status :: 4 - Beta',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: Python Software Foundation License',
      'Operating System :: MacOS :: MacOS X',
      'Operating System :: Microsoft :: Windows',
      'Operating System :: POSIX',
      'Programming Language :: Python :: 3',
    ],
)
