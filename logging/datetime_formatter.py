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
    def formatTime(self, record, datefmt="%Y/%m/%d %H:%M:%S.%f"):
        # ct = self.converter(record.created)
        # return ct.strftime(datefmt)
        return self.converter.(record_created).strftime(datefmt)


