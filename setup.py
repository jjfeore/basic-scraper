"""Setup for scraper.py."""
from setuptools import setup, find_packages

requires = [
    'ipython',
    'html5lib',
    'requests',
    'bs4',
    'pprint',
    'geocoder',
]

tests_require = [
    'pytest',
    'pytest-cov',
    'tox',
]

setup(
    name='Basic Scraper',
    desctription='Implements a scraper for the King County Health reports.',
    version='0.1',
    author='James Feore',
    author_email='jjfeore@gmail.com',
    license='MIT',
    py_modules=['scraper'],
    package_dir={'': 'src'},
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'scraper = scraper:main'
        ]
    }
)
