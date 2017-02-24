from __future__ import unicode_literals
from builtins import object


class HelloWorldTask(object):
    @staticmethod
    def perform(data):
        return "Hello world!\n"
