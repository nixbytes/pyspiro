from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pyspiro',
    version='2020.12.29',
    author='nixbytes',
    author_email='',
    description='A utility for creating spiro graphs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nixbytes/pyspiro',
    packages=find_packages('pyspiro')
)
