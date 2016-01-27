from os.path import join, dirname
import sys

with open(join(dirname(__file__), 'scrapyd/VERSION')) as f:
    version = f.read().strip()

setup_args = {
    'name': 'Scrapyd',
    'version': version,
    'url': 'https://github.com/scrapy/scrapyd',
    'description': 'A service for running Scrapy spiders, with an HTTP API',
    'long_description': open('README.rst').read(),
    'author': 'Scrapy developers',
    'maintainer': 'Scrapy developers',
    'maintainer_email': 'info@scrapy.org',
    'license': 'BSD',
    'packages': ['scrapyd'],
    'scripts': ['bin/scrapyd', 'bin/scrapyd-deploy'],
    'include_package_data': True,
    'classifiers': [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: No Input/Output (Daemon)',
        'Topic :: Internet :: WWW/HTTP',
    ],
}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
else:
    if sys.version_info < (2, 7):
        setup_args['install_requires'] = ['Twisted>=8.0,<=15.1', 'Scrapy>=0.17,<0.19', 'w3lib<1.9']
    else:
        setup_args['install_requires'] = ['Twisted>=8.0', 'Scrapy>=0.17,<0.25', 'w3lib<1.9']


setup(**setup_args)
