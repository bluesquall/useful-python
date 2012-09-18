#!/usr/bin/env python
"""
`simple-subprocess.py`
======================

A script with examples of a simple subprocess.


References:
-----------
[Python Module of the Week](http://www.doughellmann.com/PyMOTW/subprocess/)
"""

import subprocess


# just run a simple command
subprocess.call('ls -l', shell=True)

# is shell = True, then environment variables, glob patterns, etc. are supported
subprocess.call('echo $HOME', shell=True)



