#!/usr/bin/env python
from __future__ import unicode_literals
import unittest
import helloworld
import sys
import platform
import pkgutil
import os

class Test_HelloWorld(unittest.TestCase):

    def setUp(self):
        self.environ = {}
        self.klass = helloworld.HelloWorld(self.environ)

    def test__getBody(self):
        self.assertEquals("Hello World",self.klass.getBody())
        
