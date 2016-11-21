# encoding: utf-8

from sophon import log
import time


def test_ConsoleLogger():
    cl = log.ConsoleLogger()
    message = 'some message\ntesting'
    cl.debug(message)
    cl.info(message)
    cl.warn(message)
    cl.critical(message)
    cl.error(message)