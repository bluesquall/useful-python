#!/usr/bin/env python
"""
`wgetzipper.py`
===============

This ia an example application to demonstrate python's configparser.

This is a simple template for a script that should use argparse to handle 
command-line arguments.

see:  
* [python docs tutorial](http://docs.python.org/library/configparser.html)  
* [Python Module of the Week](http://www.doughellmann.com/PyMOTW/ConfigParser/)

"""

from ConfigParser import SafeConfigParser # configparser in python 3
from urllib import urlretrieve
import os, zipfile, gzip

def unzipper(instream, outstream, verbose=0):
    """Dummy method to unzip."""
    try: 
        zf = zipfile.ZipFile(instream)
    except:
        tf, header = urlretrieve(instream)
        zf = zipfile.ZipFile(tf)
    if verbose > 0: print zf.namelist()
    for f in zf.namelist():
        of = open(os.path.join(outstream,f), 'w')
        of.write(zf.read(f))
        of.close()


def gzipper(instream, outstream, verbose=0):
    """Dummy method to unzip."""
    print outstream
    gzf = gzip.open(outstream,'w')
    try:
        gzf.write(open(instream,'r').read())
    finally:
        gzf.close()


def main(inifile = 'example.ini', verbose = 0):
    """Parse the config file and perform actions it specifies."""
    parser = SafeConfigParser()
    try: parser.read(inifile.name)
    except: parser.read(inifile)
    if verbose > 0: 
        print 'verbose output'
        print parser.sections()
    for section_name in parser.sections():
        print section_name
        if verbose > 0: 
            print 'Section:', section_name
            print '  Options:', parser.options(section_name)
            for name, value in parser.items(section_name):
                print '  %s = %s' % (name, value)
        try: 
            act = parser.get(section_name, 'action')
        except Exception as e:
            raise e
        if act == 'unzip': 
            unzipper(parser.get(section_name, 'input'), 
                parser.get(section_name, 'output'),
                verbose)
        elif act == 'gzip':
            gzipper(parser.get(section_name, 'input'), 
                parser.get(section_name, 'output'),
                verbose)
        else:
            raise Exception('how do I {0}?'.format(act))


if __name__ == "__main__":
    import argparse
    # instantiate parser
    parser = argparse.ArgumentParser(description='configparser example')
    # add optional arguments
    parser.add_argument('-V', '--version', action='version', 
        version='%(prog)s 0.0.1',
        help='display version information and exit')
    parser.add_argument('-v', '--verbose', action='count', default=0,
        help='display verbose output')
    parser.add_argument('-i', '--inifile', metavar='filename', 
        type=argparse.FileType('r'), default='example.ini',
        help='configuration file')
    args = parser.parse_args()
    # call the main method to do something interesting
    main(**args.__dict__) #TODO more pythonic?
