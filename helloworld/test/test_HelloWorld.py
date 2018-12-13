#!/usr/bin/env python
from __future__ import unicode_literals
import unittest
import helloworld
import sys
import platform
import pkgutil
import os

class Test_HelloWorld(unittest.TestCase):

    def test__method1(self):
        self.assertEquals("Hello World2",helloworld.HelloWorld().method1())
        
