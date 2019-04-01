from setuptools import setup, find_packages

with open('README.md') as _f:
    _README_MD = _f.read()

_VERSION = '1.5'

setup(
    name='highlight_bot', # TODO: rename. 
    version=_VERSION,
    description='Download daily/nightly highlights',
    long_description=_README_MD,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    url='https://github.com/..../....',
    author='Wilson MacLeod',
    author_email='wilsonmacleod@gmail.com',
    packages=setup.find_packages(),
)

