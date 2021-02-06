from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pyspiro',
    version='2021.02.04',
    author='nixbytes',
    author_email='',
    description='A utility for creating spiro graphs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nixbytes/pyspiro',
    packages=find_packages('pyspiro'),
    package_dir={'':'pyspiro'},
    install_requires=[],
    entry_points={
        'console_scripts': 'pyspiro=pyspiro.main:main',
    },
)
