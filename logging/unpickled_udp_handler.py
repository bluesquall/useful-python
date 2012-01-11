"""
unpickled udp handler
=====================

sometimes you just want to send ascii text...

"""

import logging

class UnpickledDatagramHandler(logging.handlers.DatagramHandler)
    def makePickle(self, record):
        return record.message
        # return record.getMessage
        # maybe I can achieve what I want by simply overriding the pickle?
