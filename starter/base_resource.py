# -*- coding: utf-8 -*-
from __future__ import division, absolute_import
# from .auth import FakeAuth, is_allowed
from pyramid.security import Everyone
from pyramid.security import Deny


class Root(dict):
    __name__ = None
    __parent__ = None


class BaseResource(dict):
    __acl__ = [
        (Deny, Everyone, 'view'),
    ]
    __name__ = None
    __parent__ = None
    request = None

    def __init__(self, name=None, parent=None, request=None):
        self.__name__ = name
        self.__parent__ = parent
        self.request = request
