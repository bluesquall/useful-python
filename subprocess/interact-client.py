#!/usr/bin/env python
"""
`interact-client.py`
====================

A client to interact with through subprocesses.

"""
import sys
sys.stderr.write('interact-client.py: starting\n')
sys.stderr.flush()

name = raw_input('What is your name? ~>\n')
print 'Hello', name
a = float(raw_input('Please input a number. ~>\n'))
print '{0} squared is {1} and its square root is {2}\n'.format(a, a**2, a**0.5)
print 'Goodbye', name

sys.stderr.write('interact-client.py: stopping\n')
sys.stderr.flush()
