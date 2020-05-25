from setuptools import setup, find_packages


setup(name='eng_dictionary',
      version='0.0.3',
      author='Sourab Sharma',
      author_email='sharmasourab93@gmail.com',
      url='https://github.com/sharmasourab93/eng_dictionary',
      description=u'A BS4 based English Dictionary',
      packages=find_packages(),
      include_package_data=True,
      install_requires=["requests",
                        "bs4",
                        "redis",
                        ],
      classifiers=["Programming Language :: Python :: 3",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent",
                   ],
      python_requires='>=3.6',
      )
