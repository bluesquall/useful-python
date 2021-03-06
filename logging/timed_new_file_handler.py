"""
Timed New File Handler
======================

"""
import os, os.path
import time
# from datetime import datetime
import logging
from logging.handlers import BaseRotatingHandler

class TimedNewFileHandler(logging.handlers.BaseRotatingHandler):
    """
    A file handler that opens new files at specified times.
    """
    def __init__(self, filename, mode='w', when='H', prefix=True, utc=True, encoding=None, delay=0):
        """
        Open a file and use it as a stream for logging.
    
        Open a new file at specified times.
    
        By default, the time is used as a prefix on the output filename.
    
        Parameters
        ----------
    
        Returns
        -------
    
        """
        BaseRotatingHandler.__init__(self, filename, mode, encoding, delay)
        self.when = when
        self.prefix = prefix
        self.utc = utc

        if self.utc: 
            t = time.gmtime()
        else:
            t = time.localtime()


        if self.when == 'S':
            self.interval = 1
            self.tstring = '%Y%m%d_%H%M%S' #TODO allow optional tstr arg?
            self.rolloverAt = ceil(time.time() + 1)
        elif self.when == 'M':
            self.interval = 60;
            self.tstring = '%Y%m%d_%H%M'
            tList = list(t)
            tList[4] += 1
            tList[5] = 0
            tRollover = time.struct_time(tList)
            print tRollover
        elif self.when == 'H':
            self.interval = 60 * 60;
            self.tstring = '%Y%m%d_%H%M' # still keep minutes
            tList = list(t)
            tList[5] = 0
            tList[4] = 0
            tList[3] += 1
            tRollover = time.struct_time(tList)
            print tRollover
#         elif self.when == 'D':
#            self.interval = 24 * 60 * 60;
#            self.tstring = '%Y%M%D'
# TODO come back to this sometime...
        else:
            raise ValueError("Invalid rollover interval specified: %s" % self.when)
        if self.when != 'S':
            if self.utc:
                self.rolloverAt = int(time.strftime('%s', tRollover))
            else:
                self.rolloverAt = time.mktime(tRollover)
        self.openNewFile(time.time())
        
        
    def openNewFile(self, t):
        """
        Figure out the new filename and open it.
        """
        if self.utc: 
            timeTuple = time.gmtime(t)
        else:
            timeTuple = time.localtime(t)
        
        if self.stream:
            self.stream.close()
            self.stream = None

        timestr = time.strftime(self.tstring, timeTuple)
        
        if self.prefix:
            path, filename = os.path.split(self.baseFilename)
            filename = timestr + '.' + filename
            outfile = os.path.join(path, filename)
        else:
            outfile = self.baseFilename + '.' + timestr
            
        if self.encoding:
            self.stream = codecs.open(outfile, self.mode, self.encoding)
        else:
            self.stream = open(outfile, self.mode)

    def doRollover(self):
        """
        Close the open file, open a new one with the appropriate name, 
        and start writing to that.

        """
        t = time.time()
        self.rolloverAt = int(t + self.interval)
        self.openNewFile(t)


    def shouldRollover(self, record):
        """
        Determine if rollover should occur.

        The parameter (record) is ignored since the rollover is time-driven,
        but it must be included so that the method signature is preserved
        and [] can be implemented as a subclass of BaseRotatingHandler.

        """
        if int(time.time()) >= self.rolloverAt: 
            return 1
        return 0

    # no more methods should be necessary


if __name__ == "__main__":
    print 'do some demo of some sort here... move it to docstring in the future'
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG) # XXX this should always be lower than INFO

    tfmt = datefmt='%Y/%m/%d %H:%M:%S'
    mfmt = "%(asctime)s.%(msecs)s %(levelname)s %(message)s"
    # TODO the msecs shortcut above prints decimal milliseconds
    formatter = logging.Formatter(mfmt, tfmt)

    shandler = logging.StreamHandler() # console handler
    shandler.setLevel(logging.DEBUG)
    
    fhandler = TimedNewFileHandler('/tmp/tnfh-demo.log', 'w', 'M')
    fhandler.setLevel(logging.DEBUG)
    
    handlers = (shandler, fhandler,)# uhandler)
    # check the levels of all the handlers and add them to the logger
    for handler in handlers:
        if handler.level > logging.INFO: handler.setLevel(logging.INFO) 
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
    while True:
        try:
            logger.info('you should see this at time: {}'.format(time.time()))
            time.sleep(1)
        except KeyboardInterrupt:
            logger.warning('terminated by KeyboardInterrupt')
            break
