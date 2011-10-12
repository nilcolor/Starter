# -*- coding: utf-8 -*-
from __future__ import division, absolute_import

class Root(dict):
    __name__ = None
    __parent__ = None


class BaseResource(object):
    __name__ = None
    __parent__ = None
    request = None

    def __init__(self, name=None, parent=None, request=None):
        self.__name__ = name
        self.__parent__ = parent
        self.request = request


class Foo(BaseResource):
    def __getitem__(self, key):
        if key == 'bar':
            return Bar('bar', self, self.request)
        raise KeyError


class Bar(BaseResource):
    pass


def root_factory(request):
    root = Root()
    root['foo'] = Foo(name='foo', parent=root, request=request)
    return root
