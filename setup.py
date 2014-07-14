# coding=utf-8

import os
from setuptools import setup


README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-fs-trumbowyg',
    version='0.1.1',
    packages=['trumbowyg'],
    include_package_data=True,
    install_requires=[],
    author='Yuri Lya',
    author_email='yuri.lya@fogstream.ru',
    url='https://bitbucket.org/fogstream/django-fs-trumbowyg',
    license='The MIT License (MIT)',
    description='Trumbowyg (WYSIWYG editor) integration app for Django admin.',
    long_description=README,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
