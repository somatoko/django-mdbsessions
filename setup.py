from setuptools import setup
from os import path


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


packages = ['mdbsession']


setup(
    name='django-mdbsessions',
    version='0.0.1',
    packages=packages,
    description='Use MongoDB as Django session backend',
    long_description=long_description,
    author='somatoko',
    author_email='',
    url='',
    zip_safe=False,
    install_requires=[
        'django >= 1.11',
        'pymongo >= 3.2.2'
    ],
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Session',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        ],
    keywords='django mongodb session',
)
