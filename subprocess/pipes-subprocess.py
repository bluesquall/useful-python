#!/usr/bin/env python
"""
`subprocess-pipes.py`
=====================

A script with examples using subprocess and pipes.


References:
-----------
[Python Module of the Week](http://www.doughellmann.com/PyMOTW/subprocess/)
"""

import subprocess

# work like old popen3 -- separate pipes for in,out,err
print '\npopen3:'
proc = subprocess.Popen('cat -; echo "to stderr" 1>&2',
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        )
stdout_value, stderr_value = proc.communicate('through stdin to stdout')
print '\tpass through:', repr(stdout_value)
print '\tstderr      :', repr(stderr_value)

# example connecting pipe segments
import subprocess

cat = subprocess.Popen(['cat', 'index.rst'], 
                        stdout=subprocess.PIPE,
                        )

grep = subprocess.Popen(['grep', '.. include::'],
                        stdin=cat.stdout,
                        stdout=subprocess.PIPE,
                        )

cut = subprocess.Popen(['cut', '-f', '3', '-d:'],
                        stdin=grep.stdout,
                        stdout=subprocess.PIPE,
                        )

end_of_pipe = cut.stdout

print 'Included files:'
for line in end_of_pipe:
    print '\t', line.strip()
