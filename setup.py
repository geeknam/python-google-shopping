from setuptools import setup

setup(
    name='python-google-shopping',
    version='0.1',
    packages=['google_shopping'],
    license=open('LICENSE').read(),
    author='Nam Ngo',
    author_email='nam@kogan.com.au',
    url='http://blog.namis.me',
    description='Python client for Google Shopping API',
    long_description=open('README.rst').read(),
    keywords='google shopping content api merchant product',
    install_requires=['requests'],
    tests_require=['mock'],
)
