from setuptools import setup, find_packages

setup(name='eng_dictionary',
      version='0.0.2',
      author='Sourab Sharma',
      author_email='sharmasourab93@gmail.com',
      url='https://github.com/sharmasourab93/eng_dictionary',
      description='A BS4 based English Dictionary',
      long_description=open('README.md').read(),
      packages=find_packages(),
      include_package_data=True,
      install_requires=open('requirements.txt').read(),
      classifiers=["Programming Language :: Python :: 3",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent",
                   ],
      python_requires='>=3.6',
      )
