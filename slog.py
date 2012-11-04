#!/usr/bin/env python
import logging
import os

"""
First Get Path To Create Social.log using $LOGNAME environment variable
social.log is log file which will contain all logs
for filesystem implementation.
"""

path = os.path.expanduser('~/') + 'social.log'
print path
if os.path.exists(path):
    fp = open(path, "w")
    fp.close()
else:
    fp = open(path,"w")
    fp.close()

"""
Write shortcuts for all required functions
config = configuration of log messages
debug = send debug message to log file
info = just a info about something
warning = proper warning messages while running code
"""
config = logging.basicConfig
debug=logging.debug
info=logging.info
warning=logging.warning

"""
Configure Basic Configuration for all logs messages
filename = filename where log messages are to be stored
level = logging level
format = defines format of the message
"""
config(filename = path,
       level=logging.DEBUG,
       format='[%(asctime)s] - [%(funcName)s %(lineno)s] -\
%(levelname)s %(message)s',
datefmt='%m/%d/%Y %I:%M:%S %p')

"""
Uncomment lines and see results
Statements are just for test
see social.log for results.
"""
#debug("Debug")
#info("Info")
#warning("Warning")
info(path)
