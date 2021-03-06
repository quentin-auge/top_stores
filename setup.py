# coding: utf8

from setuptools import find_packages, setup

setup(name='top-stores',
      version='0.1',
      description='Aggregate store transactions',
      author='Quentin Augé',
      author_email='quentin.auge@gmail.com',
      license='closed',
      packages=find_packages(),

      python_requires='>=3.6',

      classifiers=['Programming Language :: Python :: 3 :: Only',
                   'Operating System :: MacOS',
                   'Operating System :: Unix'],

      extras_require={
          'testing': ['coverage', 'pytest', 'pytest-cov']
      },

      entry_points={
          'console_scripts': [
              'top-stores = top_stores.cli:main'
          ]
      })
