from setuptools import setup, find_packages


with open('README.rst') as f:
    README = f.read()

with open('LICENSE') as f:
    LICENSE = f.read()

setup(
    name='lolfantasy',
    version='0.1.0',
    description='Program for calculating fantasy league of legends score.',
    long_description=README,
    author='Liam Lundy',
    author_email='llundy013@gmail.com',
    url='https://github.com/liamlundy/lolfantasy',
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs'))
)
