#!/usr/bin/env python
"""
`name_is_main.py`
=================

This is a simple template for a script that should use argparse to handle 
command-line arguments.

see:  
* [python docs tutorial](http://docs.python.org/howto/argparse.html)  
* [Python Module of the Week](http://www.doughellmann.com/PyMOTW/argparse/)
* [travelingfrontiers](http://travelingfrontiers.wordpress.com/2010/11/03/simple-python-argparse-wrapper/)

to-do:  
* consider implementing a wrapper with default Linux-style command-line 
  arguments (e.g., patterned after the [travelingfrontiers] post) and call it  
  defargparse.

"""
from datetime import datetime

def main(echo = 'echo', verbose = 0, outfile = None, t = None,
        multi_word_argument = False):
    """Do something interesting with the arguments."""
    if t: 
        timestamp = datetime.utcnow()
    else: 
        timestamp = None
    if timestamp:
        #TODO some kind of switch for timestamp format given different verbosity
        timestr = timestamp.isoformat() + '\t'
    else:
        timestr = '' # an empty string
    rstr = '{timestr}{echo}\n'.format(timestr = timestr, echo = echo)
    try:
        outfile.write(rstr)
        outfile.close()
    except:
        print rstr
    if multi_word_argument:
        print "multi-word argument:", multi_word_argument
    

if __name__ == "__main__":
    import argparse
    # instantiate parser
    parser = argparse.ArgumentParser(description='argparse example', 
        prefix_chars='-+')
    # add positional arguments
    parser.add_argument('echo', help='echo the string you use here')
    # add optional arguments
    parser.add_argument('-V', '--version', action='version', 
        version='%(prog)s 0.0.1',
        help='display version information and exit')
    parser.add_argument('-v', '--verbose', action='count', default=0,
        help='display verbose output')
    parser.add_argument('-o', '--outfile', metavar='filename', 
        type=argparse.FileType('wt'), help='output file')
    parser.add_argument('-m','--multi-word-argument',
        type=str, help='argument named with multiple words')
    # add options with prefixes
    parser.add_argument('-t', action="store_false", default=None,
        help='do not print timestamp')
    parser.add_argument('+t', action="store_true", default=None,
        help='print timestamp')
    # mutually exclusive options...
    # TODO UTC or local or specified -- assumes -t
    # actually parse the arguments
    args = parser.parse_args()
    # call the main method to do something interesting
    main(**args.__dict__) #TODO more pythonic?
