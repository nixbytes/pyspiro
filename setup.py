from setuptools import setup, find_packages

with open('README.md', encoding='UTF-8') as f:
  readme = f.read()

setup(
    name='pyspiro',
    version='2021.02.05',
    description='Command line user for spiro designs',
    long_description=readme,
    author='nixbytes',
    author_email='real8686@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': 'pyspiro=pyspiro.cli:main',
    },
)
