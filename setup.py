from setuptools import setup, find_packages

setup(
    name='excel_modifier',
    version='0.1',
    author='DrCino',
    author_email='khaled775057605@gmail.com',
    description='A package for editing Excel files for specific files',
    long_description='Detailed description of your package',
    long_description_content_type='text/markdown',
    url='https://github.com/DrCinco730/excel_modifier',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
    ],
)
