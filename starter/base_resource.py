# -*- coding: utf-8 -*-
from __future__ import division, absolute_import

class Root(dict):
    __name__ = None
    __parent__ = None


class BaseResource(dict):
    __name__ = None
    __parent__ = None
    request = None

    def __init__(self, name=None, parent=None, request=None):
        self.__name__ = name
        self.__parent__ = parent
        self.request = request
