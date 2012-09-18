#!/usr/bin/env python
"""
`subprocess-interact.py`
========================

A script with examples using subprocess continuing to interact.


References:
-----------
[Python Module of the Week](http://www.doughellmann.com/PyMOTW/subprocess/)
"""

import subprocess

# use communicate and print at the end
proc = subprocess.Popen('python interact-client.py',
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        )
stdout_value, stderr_value = proc.communicate('\n'.join(('Herbie','53',' ')))
print '\tstdout:\n{}'.format(stdout_value)
# remember, communicate waits until the process exits before returning

# write and read pipes as you go
proc = subprocess.Popen('python interact-client.py',
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        )
#print '\tstdout 0:', proc.stdout.readline()
proc.stdin.write('Herbie Hancock\n') # you may need a newline
#print '\tstdout 1:', proc.stdout.readline()
proc.stdin.write('{0:01d}\n'.format(3))
#print '\tstdout 2:', proc.stdout.readline()
stdout_value, stderr_value = proc.communicate()
print '\tstdout -1:', repr(stdout_value)



