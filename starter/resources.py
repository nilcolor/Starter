# -*- coding: utf-8 -*-
from __future__ import division, absolute_import
from .base_resource import Root, BaseResource
from pyramid.traversal import resource_path

################################################################################
# Root resource level
class AppRoot(Root):
    def __init__(self, request):
        self.update({
            "orders": OrderCollection(name='orders', parent=self, request=request)
        })

################################################################################
# Order resources
class OrderCollection(BaseResource):
    def __init__(self, name=None, parent=None, request=None):
        super(OrderCollection, self).__init__(name=name, parent=parent, request=request)
        self.update({
            'bar': Bar('bar', self, self.request),
            'zar': Zar('zar', self, self.request),
        })

    def __getitem__(self, key):
        print "Try to get #%s for %s" % (key, resource_path(self))
        subresource = self.get(key, key)

        if subresource == key:
            return Order(key, self, self.request)
        else:
            return subresource


class Order(BaseResource):
    def __init__(self, name=None, parent=None, request=None):
        super(Order, self).__init__(name=name, parent=parent, request=request)
        self.order_id = name

    def __getitem__(self, key):
        print "Try to get #%s for %s" % (key, resource_path(self))
        subresource = self.get(key, key)

        if subresource == key:
            raise KeyError

        return None

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
