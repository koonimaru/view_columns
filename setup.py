#from distutils.core import setup
from setuptools import setup, find_packages
from distutils.extension import Extension
import re
import os
import codecs

#print(find_version("deepgmap", "__init__.py"))
setup(
    name='view_columns',
    #version=VERSION,
    version="1.0.0",
    description='Viewing a file containing a lot of columns',
    author='Koh Onimaru',
    author_email='koh.onimaru@gmail.com',
    url='',

    scripts=['bin/view_columns',
                   ],
    #packages=find_packages(),
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: Apache Software License ',
        'Operating System :: POSIX :: Linux',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ]
)

