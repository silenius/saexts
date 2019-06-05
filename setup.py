import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'SQLAlchemy',
]

setup(name='saexts',
      version='0.1.3',
      description='saexts',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Topic :: Database",
        "License :: OSI Approved :: BSD License",
        ],
      author='Julien Cigar',
      author_email='julien@perdition.city',
      url='https://github.com/silenius/saexts',
      keywords='sqlalchemy serialize',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      )
