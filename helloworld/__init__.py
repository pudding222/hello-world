import pkgutil
import platform

from .HelloWorld import HelloWorld

__title__ = 'Helloworld'
__version__ = "1"
__author__ = 'dan'
__license__ = 'MIT'
__copyright__ = '2018'

version_information = ["Python",
                       platform.python_version(),                       
                       platform.platform(),
                       "1",
                       ]
version_info = "::".join(version_information)
