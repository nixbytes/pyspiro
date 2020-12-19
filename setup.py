from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pyspiro',
    version='0.1.0',
    author='nixbytes',
    author_email='',
    description='A utility for creating spiro graphs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    packages=find_packages('src')
)