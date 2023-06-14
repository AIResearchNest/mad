from setuptools import setup, setuptools 
from mad._version import __version__

setup(
    name = 'Multi Agent Development API',
    packages = setuptools.find_packages(),
    author = 'CURI Research',
    version = __version__
    )