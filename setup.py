#from setuptools import setup
from distutils.core import setup

setup(name='eng_dictionary',
      version='1.0',
      author='Sourab Sharma',
      author_email='sharmasourab93@gmail.com',
      license='MIT',
      url='https://github.com/sharmasourab93/eng_dictionary',
      description='A BS4 based English Dictinonary',
      long_description=open('README.txt').read(),
      packages=['eng_dictionary'],
      classifiers=["Programming Language:: Python","Programming Language :: Python :: 3"],      
      )
