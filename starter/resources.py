# -*- coding: utf-8 -*-
from __future__ import division, absolute_import
from .base_resource import Root, BaseResource

################################################################################
# Root resource level
class Foo(BaseResource):
    def __init__(self, name=None, parent=None, request=None):
        super(Foo, self).__init__(name=name, parent=parent, request=request)
        self.update({
            'bar': Bar('bar', self, self.request),
            'zar': Zar('zar', self, self.request),
        })

################################################################################
# Bar childrens
class Bar(BaseResource):
    def __init__(self, name=None, parent=None, request=None):
        super(Bar, self).__init__(name=name, parent=parent, request=request)
        self.update({
            'go': Go('go', self, self.request),
        })

class Go(BaseResource):
    pass


################################################################################
# Zar branch
class Zar(BaseResource):
    pass


################################################################################
# Root factory
def root_factory(request):
    root = Root()
    root['foo'] = Foo(name='foo', parent=root, request=request)
    return root
