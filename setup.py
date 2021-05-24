#!/usr/bin/env python


import os

# allow setup.py to be run from any path
# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# if __name__ == "__main__":
import setuptools

setuptools.setup(
    name='staff_models',
    version='1.0.1',
    packages=setuptools.find_packages(),
    install_requires=[
        'image-utils @ git+https://github.com/reimibeta/django-image-utils.git',
        'datetime-utils @ git+https://github.com/reimibeta/django-datetime-utils.git',
        'html-render-utils @ git+https://github.com/reimibeta/django-html-render-utils.git',
    ]
    # scripts=['manage.py']
)
