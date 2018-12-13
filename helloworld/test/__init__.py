import unittest
import os
__author__ = 'Dan'


def all():
    path = os.path.dirname(os.path.realpath(__file__))
    return unittest.TestLoader().discover(path)
