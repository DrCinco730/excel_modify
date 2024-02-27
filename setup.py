from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='excel_modify',
    version='1.1',
    author='DrCino',
    author_email='khaled775057605@gmail.com',
    description='A package for editing Excel files for specific files',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DrCinco730/excel_modifier',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
    ],
)
