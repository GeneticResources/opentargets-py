#!/usr/bin/env python

from distutils.core import setup

setup(name='opentargets',
      version='1.2.0b2',
      description='Client for Open Targets REST API at targetvalidation.org',
      author='Andrea Pierleoni',
      author_email='andreap@ebi.ac.uk',
      maintainer='Open Targets Core Team',
      maintainer_email='support@targetvalidation.org',
      url='https://github.com/CTTV/opentargets-py',
      packages=['opentargets'],
      license='Apache 2.0',
      download_url='https://github.com/CTTV/opentargets-py/tarball/1.2.0a1',
      keywords = ['opentargets', 'bioinformatics', 'python3'],
      install_requires=[
          'requests==2.11.1',
          'cachecontrol==0.11.6',
          'hyper==0.7.0',
          'PyYAML'],
      extras_require={
          'tests': [
              'nose',
              'pandas',
              'xlwt'
              ],
          'docs': [
              'sphinx >= 1.4',
              'sphinx_rtd_theme']}
      )