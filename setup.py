from setuptools import setup

setup(
    name='sd-code-test',
    version='1.0.0',
    description='Code test',
    author='Kevin Smith',
    author_email='kevinsmith.kis@gmail.com',
    setup_requires=['flake8'],
    tests_require=['pytest'],
    packages=['app']
)