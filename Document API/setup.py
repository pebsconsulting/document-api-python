try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='tableaudocumentapi',
    version='0.0.1',
    summary='A Python module for working with Tableau files.',
    author='Tableau Software',
    author_email='github@tableau.com',
    url='https://github.com/tableau/tableausdk-python',
    py_modules=['tableaudocumentapi'],
    license='MIT',
    description='A Python module for working with Tableau files.'
)
