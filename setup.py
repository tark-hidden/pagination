"""
Pagination
----------

Framework agnostic, very simple bootstrap-based URL-generator for pagination. 

Implements http://codereview.stackexchange.com/q/15235/
"""
from setuptools import setup

setup(
    name='Pagination',
    version='0.1',
    url='https://github.com/tark-hidden/pagination',
    license='BSD',
    author='Tark',
    maintainer="Tark",
    author_email='tark.hidden@gmail.com',
    description='Simple and fast bootstrap-based pagination',
    long_description=__doc__,
    py_modules=['pagination'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]    
)