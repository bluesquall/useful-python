"""
datetime formatter
==================


note: inspired by: http://stackoverflow.com/questions/6290739/python-logging-use-milliseconds-in-time-format
"""

import logging
from datetime import datetime

class DatetimeFormatter(logging.Formatter):
    converter = datetime.fromtimestamp 

    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        if datefmt:
            s = ct.strftime(datefmt)
        else: # still use ISO8061
            t = ct.strftime("%Y-%m-%d %H:%M:%S")
            s = "%s,%03d" % (t, record.msecs)
        return s


class UTCDatetimeFormatter(DatetimeFormatter):
    converter = datetime.utcfromtimestamp


class DSLDatetimeFormatter(UTCDatetimeFormatter):
    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        # ignore the datefmt kwarg
        return "%s.%03d" % (ct.strftime("%Y/%m/%d %H:%M:%S"), record.msecs)
        # TODO new string format

if __name__ == "__main__":
    mfmt = "%(asctime)s %(levelname)s %(message)s"
    
    #formatter = DatetimeFormatter(mfmt, "%Y/%m/%d %H:%M:%S.%f")
    #formatter = UTCDatetimeFormatter(mfmt)
    formatter = DSLDatetimeFormatter(mfmt)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    shandler = logging.StreamHandler()
    shandler.setLevel(logging.DEBUG)
    shandler.setFormatter(formatter)
    logger.addHandler(shandler)

    logger.info('How now brown cow?')
