from setuptools import setup, find_packages

setup(
    name='pyBlufi',
    version='0.0.1',
    description="Python utility to interface with esp32 Blufi component.",
    packages=find_packages(),
    install_requires=[
        'cryptography>=45.0.7',
        'bleak>=1.1.1'
    ],
)
