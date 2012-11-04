#!/usr/bin/python
#This Just Template Not Complete Setup.py
import sys
from distutils.core import setup
setup(
    name='sharefs',
    version='1.0',
    description='Treat Social sites As a file system',
    author='Sanket Sudake, Sagar Rakshe',
    author_email='sanketsudake@gmail.com',
    license='GPLv2',
    py_modules=['choose.py', 'internet.py', 'main.py', 'notify.py','slog.py',
                'socialfs.py', 'social.py','stest.py'
            ],
    scripts=['socialrun.sh'],
    )
#
# Final User will just run socialrun command to use application
# See socialrun.sh for more
# To be added
#
#url =
#packages =
